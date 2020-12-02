__author__ = 'Jiri Fajtl'
__email__ = 'ok1zjf@gmail.com'
__version__= '4.8'
__status__ = "Research"
__date__ = "23/1/2018"
__license__= "MIT License"

import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
# os.environ["CUDA_VISIBLE_DEVICES"]="0"

import time
import torch
from torchvision import transforms
from torch.autograd import Variable
import cv2
import numpy as np

from memory.lamem2 import  *
from memory.amnet_model import *
import memory.amnet_model as amnet_model
from memory.config import *
import shutil


# ------------------------------------------------------------------------------------------

class PredictionResult():
    def __init__(self):
        self.rc = 0
        self.mse  = 0
        self.predictions = []
        self.targets = []
        self.outputs = []
        self.attention_masks = []
        self.inference_took = 0
        self.image_names = []
        self.images = None # If source images are pre-loaded this atribute will hold their bitmaps

    def write_stdout(self):
        pred = np.mean(self.predictions)

        return pred

class AMNet:

    def __init__(self):
        self.logger = None
        self.total_time = 0
        self.model = None
        self.lr = 0
        self.optimizer = None
        self.data_dir = 'data'
        self.show_delay = 0

        self.test_transform = None
        self.train_transform = None
        return

    def init(self, hps):
        self.hps = hps

        self.experiment_path = os.path.join(self.data_dir, hps.experiment_name)

        if hps.front_end_cnn == 'ResNet50FT':
            model = getattr(amnet_model, hps.front_end_cnn)()
        else:
            core_cnn = getattr(amnet_model, hps.front_end_cnn)()
            model = AMemNetModel(core_cnn, hps, a_res=14, a_vec_size=1024)

        rnd_seed = 12345
        np.random.seed(rnd_seed)
        torch.manual_seed(rnd_seed)

        if hps.use_cuda:
            torch.cuda.set_device(hps.cuda_device)
            print("Curent CUDA device: ", torch.cuda.current_device())
            torch.cuda.manual_seed(rnd_seed)


        self.model = model
        self.init_transformations()
        self.load_checkpoint(self.hps.model_weights)
        return

    def get_experiment_path(self):
        return self.experiment_path

    def init_transformations(self):

        if self.hps.torchvision_version_major == 0 and self.hps.torchvision_version_minor < 2:
            _resize = transforms.Scale
            _rnd_resize_crop = transforms.RandomSizedCrop
        else:
            _resize = transforms.Resize
            _rnd_resize_crop = transforms.RandomResizedCrop

        self.train_transform = transforms.Compose([
            _resize([264, 264]),
            _rnd_resize_crop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=self.hps.img_mean, std=self.hps.img_std)
        ])

        # Test
        self.test_transform = transforms.Compose([
            _resize([224, 224]),
            transforms.ToTensor(),
            transforms.Normalize(mean=self.hps.img_mean, std=self.hps.img_std)
        ])

        return

    def load_checkpoint(self, filename):

        if filename.strip() == '':
            return False

        try:
            print('Loading checkpoint: ', filename)
            cpnt = torch.load(filename, map_location=lambda storage, loc: storage)
            self.experiment_path, filename = os.path.split(filename)
        except FileNotFoundError:
            print("Cannot open file: ", filename)
            self.model_weights_current = ''
            return False

        try:
            self.model.load_weights(cpnt['model'])
        except:
            self.model.load_state_dict(cpnt['model'])

        return True


    def postprocess(self, output, outputs):

        if self.hps.last_step_prediction:
            output = outputs[:,-1:]
        else:
            output = (outputs).sum(1)
            output = output / outputs.shape[1]

        output /= self.hps.target_scale
        output = output + self.hps.target_mean

        if self.hps.last_step_prediction:
            outputs[:] = 0
            outputs[:,-1:] = output
        else:
            outputs = (outputs / (outputs.shape[1] * self.hps.target_scale)) + self.hps.target_mean / outputs.shape[1]

        return output, outputs

    def predict(self, test_loader):

        self.model.eval()

        if self.hps.use_cuda:
            self.model.cuda()

        pr = PredictionResult()

        predictions = []
        targets = []
        output = None
        outputs = None
        alphas = None
        img_names = []

        batches = 0
        img_inference_took = 0

        for data, target, names in test_loader:

            for val in target:
                targets.append(val)

            img_names += names

            target = target.float()
            if self.hps.use_cuda:
                data, target = data.cuda(), target.cuda()

            data, target = Variable(data, volatile=True), Variable(target)

            # print(batches, len(predictions))
            batch_inference_start = time.time()
            output_, outputs_, alphas_ = self.model(data)
            batch_inference_took = time.time() - batch_inference_start
            img_inference_took += batch_inference_took / data.size(0)
            batches += 1

            outputs_ = outputs_.cpu().data.numpy()
            output_ = None if output_ is None else output_.cpu().data.numpy()
            alphas_ = alphas_.cpu().data.numpy()

            memity, outputs_ = self.postprocess(output_, outputs_)

            for val in memity:
                predictions.append(val)

            # Append results overl all batches
            output = output_ if output is None else np.concatenate(output, output_)
            outputs = outputs_ if outputs is None else np.concatenate(outputs, outputs_)

            alphas = alphas_ if alphas is None else np.concatenate(alphas, alphas_)

        if test_loader.dataset.valid_labels:
            rc, mse = test_loader.dataset.getRankCorrelationWithMSE(predictions, gt=targets)
        else:
            rc, mse = None, None


        pr.rc = rc
        pr.mse  = mse
        pr.image_names = img_names
        pr.predictions = predictions
        pr.targets = targets
        pr.outputs = outputs
        pr.attention_masks = alphas
        pr.inference_took = img_inference_took / batches

        return pr

    def predict_memorability(self, images_path):

        # Use the data.Dataset class to simplify preprocesing and batch generation on multicore architectures
        dataset = LaMem2(split=images_path, # Load all images if the split points to a directory otherwise expects
                         transform=self.test_transform)

        batch_size = self.hps.test_batch_size
        if len(dataset.data) < batch_size:
            batch_size = len(dataset.data)
            print("Reducing batch size from ", self.hps.test_batch_size, "to",batch_size)

        num_workers = 8
        loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=False, drop_last=False,
                                                  num_workers=num_workers)

        pr = self.predict(loader)
        print(pr)
        return pr

# if __name__ == "__main__":
#     ge_pkg_versions
#     amnet = AMNet()
#     amnet.predict_memorability('F:/PythonProjects/AMNet-master/datasets/lamem/images')

