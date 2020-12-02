class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = '/home/zlj/PycharmProjects/py_torch1/UCF-101'

            # Save preprocess data into output_dir
            output_dir = '/home/zlj/PycharmProjects/py_torch1/VAR/ucf101'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return '/home/zlj/PycharmProjects/py_torch1/c3d-pretrained.pth'