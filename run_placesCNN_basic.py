import torch
from torch.autograd import Variable as V
import torchvision.models as models
from torchvision import transforms as trn
from torch.nn import functional as F
import os
from PIL import Image
import cv2
# import matplotlib.pyplot as plt
# plt.switch_backend('agg')


def Places(video):
    # th architecture to use
    arch = 'resnet18'

    # load the pre-trained weights
    model_file = '%s_places365.pth.tar' % arch
    if not os.access(model_file, os.W_OK):
        weight_url = 'http://places2.csail.mit.edu/models_places365/' + model_file
        os.system('wget ' + weight_url)

    model = models.__dict__[arch](num_classes=365)
    checkpoint = torch.load(model_file, map_location=lambda storage, loc: storage)
    state_dict = {str.replace(k,'module.',''): v for k,v in checkpoint['state_dict'].items()}
    model.load_state_dict(state_dict)
    model.eval()

    # load the image transformer
    centre_crop = trn.Compose([
            trn.Resize((256,256)),
            trn.CenterCrop(224),
            trn.ToTensor(),
            trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # load the class label
    file_name = 'categories_places365.txt'
    if not os.access(file_name, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/categories_places365.txt'
        os.system('wget ' + synset_url)
    classes = list()
    with open(file_name) as class_file:
        for line in class_file:
            classes.append(line.strip().split(' ')[0][3:])
    classes = tuple(classes)

    cap = cv2.VideoCapture(video)
    retaining = True

    clip = []
    Prob = []
    Class = []
    #Prob = np.array()
    while retaining:
        retaining, frame = cap.read()
        if not retaining and frame is None:
            continue
    # forward pass
        frame_img = Image.fromarray(frame)
        input_img = V(centre_crop(frame_img).unsqueeze(0))
        logit = model.forward(input_img)
        h_x = F.softmax(logit, 1).data.squeeze()
        probs, idx = h_x.sort(0, True)

        # cv2.putText(frame, classes[idx[0]], (20, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 1)
        # cv2.putText(frame, "prob: %.4f" % probs[0], (20, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 1)
        # clip.pop(0)
        #
        # cv2.imshow('result', frame)
        # cv2.waitKey(30)

        for i in range(0,3):
            #var = (Class == classes[idx[i]] ).any()
            if classes[idx[i]] in Class:
                indexnum = Class.index(classes[idx[i]])
                if Prob[indexnum] <= probs[i]:
                    Prob[indexnum] = probs[i]
            else:
                Class.append(classes[idx[i]])
                Prob.append(probs[i])

    return Class,Prob
    # max5index = map(Prob.index, heapq.nlargest(5, Prob))
    # print('{} prediction on {}'.format(arch, video))
    #     #output the prediction
    # for i in list(max5index):
    #     print(list(max5index))
    #     print('{:.3f} -> {}'.format(Prob[i], Class[i]))


