from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtMultimediaWidgets import QVideoWidget
from test import Ui_MainWindow
from myVideoWidget import myVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import load_model
from statistics import mode
from emotion_utils.datasets import get_labels
from emotion_utils.inference import detect_faces
from emotion_utils.inference import draw_text
from emotion_utils.inference import draw_bounding_box
from emotion_utils.inference import apply_offsets
from emotion_utils.inference import load_detection_model
from emotion_utils.preprocessor import preprocess_input
from memory.memorability import memory
#print(matplotlib.get_backend())
sys.path.append('.\\fashion')
from fashion.predict import *
from fashion.utils import *
from fashion.config import *
#print(matplotlib.get_backend())
import sys
import inference
import qtawesome
import webbrowser
# from tensorflow import keras
import os
# os.environ['KERAS_BACKEND']='tensorflow'
import xlrd
import random,time
import shutil
import cv2
import numpy as np
import heapq
import os
from PIL import Image
import cv2
import keras
#import matplotlib.pyplot as plt


import run_placesCNN_basic

class myMainWindow(Ui_MainWindow,QMainWindow):

    def __init__(self):      #初始化
        super(Ui_MainWindow, self).__init__()
        self.init_ui()
        self.n = 1
        self.videoFullScreen = False   # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()   # 创建一个全屏的widget
        self.videoFullScreenWidget.setFullScreen(1)
        self.videoFullScreenWidget.hide()               # 不用的时候隐藏起来
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的

        self.pushButton_11.clicked.connect(self.openVideoFile)   # 打开视频文件按钮
        self.pushButton_52.clicked.connect(self.camera)
        # self.pushButton_23.clicked.connect(self.playVideo)       # continue

        self.pushButton_35.clicked.connect(self.method)       # pause
        self.player.positionChanged.connect(self.changeSlide)      # change Slide
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)  #双击响应
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)   #双击响应
        self.pushButton_7.clicked.connect(self.scene)
        self.pushButton_8.clicked.connect(self.BehaviorResult)  #行为识别
        self.pushButton_25.clicked.connect(self.emotion)
        self.pushButton_36.clicked.connect(self.memorize)
        self.pushButton_10.clicked.connect(self.Dfashion)
        self.pushButton_34.clicked.connect(self.ChooseModel)  #选择模型
        self.pushButton_18.clicked.connect(self.Open_url)
        self.pushButton_23.clicked.connect(self.next_video)  # 播放下一个视频
        self.pushButton_33.clicked.connect(self.last_video)  # 播放下一个视频
        self.pushButton_41.clicked.connect(self.Accuracy)
        self.pushButton_42.clicked.connect(self.ROC)
        self.pushButton_43.clicked.connect(self.FV)
        self.pushButton_44.clicked.connect(self.Return)

    def ChooseModel(self):
        if self.comboBox.currentText() == "事件检测":
            self.BehaviorResult()
        elif self.comboBox.currentText() == "情感分析":
            self.emotion()
        elif self.comboBox.currentText() == "场景估计":
            self.scene()
        elif self.comboBox.currentText() == "流行度分析":
            self.popularityAnalysis()
        elif self.comboBox.currentText() == "记忆度分析":
            self.memorize()
        else:
            self.Dfashion()

    def scene(self):
        self.wgt_video.raise_()
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        (Class,Prob)=run_placesCNN_basic.Places(self.fileName)
        max3index = map(Prob.index, heapq.nlargest(3, Prob))
        sce=list(max3index)
        #     #output the prediction
        var=True
        delay=30
        while var:
            if (self.pushButton_11.isDown()== True)  or (self.pushButton_52.isDown()== True) or (self.pushButton_8.isDown()==True)or (self.pushButton_33.isDown()== True) or (self.pushButton_23.isDown()== True) or (self.pushButton_36.isDown()== True)  :
                var = False
                self.label_51.clear()
            else:
                cap = cv2.VideoCapture(self.fileName)
                while cap.isOpened():  # True:]

                    ret, bgr_image = cap.read()
                    if ret == False or (self.pushButton_11.isDown() == True)  or (self.pushButton_8.isDown()==True)or (self.pushButton_33.isDown()== True) or (self.pushButton_23.isDown()== True) or (self.pushButton_36.isDown()== True)  :
                        self.label_51.clear()
                        self.label_52.clear()
                        self.wgt_video.raise_()
                        break
                    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

                    text = Class[sce[0]] + ": %.3f" % Prob[sce[0]] + '\n' + Class[sce[1]] + ": %.3f" % Prob[sce[1]]+ '\n' + Class[sce[2]] + ": %.3f" % Prob[sce[2]]
                    prob = "%.3f" % Prob[sce[0]]
                    self.output_class_9.setText(Class[sce[0]])
                    self.output_class_10.setText(prob)
                    y0, dy = 14, 20
                    for i, txt in enumerate(text.split('\n')):
                        y = y0 + i * dy
                        sce_img=cv2.putText(rgb_image, txt, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

                    rgb_image = cv2.resize(sce_img,(340,260))
                    img = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
                    self.label_51.raise_()
                    self.label_51.setPixmap(QPixmap.fromImage(img))
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break


    def popularityAnalysis(self):
        self.emotion()
    def memorize(self):
        self.wgt_video.raise_()
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        result = memory(self.fileName)
        Result = "%.4f" % result
        self.output_class_9.setText(Result)
    def Dfashion(self):
        filename = self.fileName
        Pred(filename)
        # shutil.rmtree('D:/Python/Projects/pyqt5_V4.0/pyqt5_V4.0/fashion/dataset_prediction/images/')
        # os.makedirs('D:/Python/Projects/pyqt5_V4.0/pyqt5_V4.0/fashion/dataset_prediction/images/')
        # # 保存图片的路径
        # # savedpath = filename.split('.')[0] + '/'
        # savedpath = 'D:/Python/Projects/pyqt5_V4.0/pyqt5_V4.0/fashion/dataset_prediction/images/'
        # isExists = os.path.exists(savedpath)
        # if not isExists:
        #     os.makedirs(savedpath)
        #     print('path of %s is build' % (savedpath))
        # else:
        #     print('path of %s already exist and rebuild' % (savedpath))
        #
        # # 视频帧率12
        # fps = 12
        # # 保存图片的帧率间隔
        # count = 60
        #
        # # 开始读视频
        # videoCapture = cv2.VideoCapture(filename)
        # i = 0
        # j = 0
        #
        # while True:
        #     success, frame = videoCapture.read()
        #     i += 1
        #     if (i % count == 0):
        #         # 保存图片
        #         j += 1
        #         #FName = filename.split('/')[3]
        #         savedname = 'Fashion' + '-' + str(j) + '-' + str(i) + '.jpg'
        #         cv2.imwrite(savedpath + savedname, frame)
        #         print('image of %s is saved' % (savedname))
        #     if not success:
        #         print('video is all read')
        #         break
        #
        # init()
        # images_path_name = get_images()
        #
        # # resize_image(images_path_name)
        # # images_path_name = get_images()
        #
        # bboxes = get_bbox(images_path_name)
        # logging.debug('bboxes {}'.format(bboxes))
        # # display_bbox(images_path_name, bboxes)
        # # shutil.rmtree('D:/Python/Projects/pyqt5_V4.0/pyqt5_V4.0/fashion/dataset_prediction/crops/')
        # # os.makedirs('D:/Python/Projects/pyqt5_V4.0/pyqt5_V4.0/fashion/dataset_prediction/crops/')
        # image_crops, image_crops_name = crop_bbox(images_path_name, bboxes)
        # logging.debug('image_crops {}'.format(len(image_crops)))
        # # logging.debug('image_crops {}'.format(image_crops))
        # # logging.debug('image_crops_name {}'.format(image_crops_name))
        #
        # # for index, image_crop in enumerate(image_crops):
        # predict_model(image_crops, image_crops_name)

    def BehaviorResult(self):
        self.wgt_video.raise_()
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        result = inference.predict_c3d(self.fileName)
        self.output_class_9.setText(result[0])
        self.output_class_10.setText(result[1])

    def camera(self):
        self.fileName = 0
        cap = cv2.VideoCapture(self.fileName)
        self.player.pause()
        while cap.isOpened():  # True:
            ret, bgr_image = cap.read()
            if ret == False or (self.pushButton_11.isDown() == True) :
                self.label_51.clear()
                self.label_52.clear()
                self.wgt_video.raise_()
                break
            rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
            rgb_image = cv2.resize(rgb_image,(340,360))
            img = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
            self.label_52.raise_()
            self.label_52.setPixmap(QPixmap.fromImage(img))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    def emotion(self):
        self.wgt_video.raise_()
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        keras.backend.clear_session()
        # parameters for loading data and images
        emotion_model_path = './emotionModels/emotion_model.hdf5'
        emotion_labels = get_labels('fer2013')
        # hyper-parameters for bounding boxes shape
        frame_window = 10
        emotion_offsets = (20, 40)
        # loading models
        face_cascade = cv2.CascadeClassifier('./emotionModels/haarcascade_frontalface_default.xml')
        emotion_classifier = load_model(emotion_model_path)
        # getting input model shapes for inference
        emotion_target_size = emotion_classifier.input_shape[1:3]
        # starting lists for calculating modes
        emotion_window = []
        var = True
        # starting video streaming
        # Select video or webcam feed
        while var:
            if (self.pushButton_11.isDown()== True)  or (self.pushButton_52.isDown()== True) or (self.pushButton_8.isDown()==True) or (self.pushButton_33.isDown()== True) or (self.pushButton_23.isDown()== True)or (self.pushButton_36.isDown()== True)  :
                var = False
                self.label_51.clear()
            else:
                cap = cv2.VideoCapture(self.fileName)
                while cap.isOpened():  # True:
                    ret, bgr_image = cap.read()
                    # bgr_image = video_capture.read()[1]
                    if ret == False or (self.pushButton_11.isDown()== True) or (self.pushButton_52.isDown()== True) or(self.pushButton_8.isDown()==True) or (self.pushButton_33.isDown()== True) or (self.pushButton_23.isDown()== True) or (self.pushButton_36.isDown()== True)  :
                        self.label_51.clear()
                        self.wgt_video.raise_()
                        break
                    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
                    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

                    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
                                                          minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
                    for face_coordinates in faces:
                        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
                        gray_face = gray_image[y1:y2, x1:x2]
                        try:
                            gray_face = cv2.resize(gray_face, (emotion_target_size))
                        except:
                            continue
                        gray_face = preprocess_input(gray_face, True)
                        gray_face = np.expand_dims(gray_face, 0)
                        gray_face = np.expand_dims(gray_face, -1)
                        emotion_prediction = emotion_classifier.predict(gray_face)
                        emotion_probability = np.max(emotion_prediction)
                        emotion_label_arg = np.argmax(emotion_prediction)
                        emotion_text = emotion_labels[emotion_label_arg]
                        emotion_window.append(emotion_text)

                        if len(emotion_window) > frame_window:
                            emotion_window.pop(0)
                        try:
                            emotion_mode = mode(emotion_window)
                        except:
                            continue

                        if emotion_text == 'angry':
                            color = emotion_probability * np.asarray((255, 0, 0))
                        elif emotion_text == 'sad':
                            color = emotion_probability * np.asarray((0, 0, 255))
                        elif emotion_text == 'happy':
                            color = emotion_probability * np.asarray((255, 255, 0))
                        elif emotion_text == 'surprise':
                            color = emotion_probability * np.asarray((0, 255, 255))
                        else:
                            color = emotion_probability * np.asarray((0, 255, 0))

                        color = color.astype(int)
                        color = color.tolist()

                        draw_bounding_box(face_coordinates, rgb_image, color)
                        draw_text(face_coordinates, rgb_image, emotion_mode,
                                  color, 0, 45, 1, 1)
                        self.output_class_9.setText(emotion_text)
                    if self.fileName == 0:
                        rgb_image = cv2.resize(rgb_image, (340, 360))
                        img = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
                        self.label_52.raise_()
                        self.label_52.setPixmap(QPixmap.fromImage(img))
                    else:
                        rgb_image = cv2.resize(rgb_image, (340, 260))
                        img = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
                        self.label_51.raise_()
                        self.label_51.setPixmap(QPixmap.fromImage(img))

                    if cv2.waitKey(25) & 0xFF == ord('q'):
                       break

    def replace_char(self, string, char, index):  # string为原字符，char是插入字符，index是指定位置
        string = list(string)
        string[index] = char
        return ''.join(string)

    def next_video(self):            # 播放下一个视频
        self.label_51.clear()
        self.label_52.clear()
        self.wgt_video.raise_()
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        index = self.fileName[-5]
        num = str(int(index) + 1)
        fileName = self.replace_char(self.fileName, num, -5)
        if os.path.exists(fileName):
            self.fileName=fileName
            self.mediaList = QMediaPlaylist()
            self.mediaList.addMedia(QMediaContent(QUrl(self.fileName)))
            self.player.setPlaylist(self.mediaList)
            self.mediaList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            self.player.play()  # 播放视频
            self.Process_ran()
            self.display_infor()

        else:
            self.mediaList = QMediaPlaylist()
            self.mediaList.addMedia(QMediaContent(QUrl(self.fileName)))
            self.player.setPlaylist(self.mediaList)
            self.mediaList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            self.player.play()  # 播放视频
            self.display_infor()

    def last_video(self):     #播放上一个视频
        self.label_51.clear()
        self.label_52.clear()
        self.wgt_video.raise_()
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        name = self.fileName
        if int(self.fileName[-5]) == 1:
            self.mediaList = QMediaPlaylist()
            self.mediaList.addMedia(QMediaContent(QUrl(self.fileName)))
            self.player.setPlaylist(self.mediaList)
            self.mediaList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            self.player.play()  # 播放视频
            self.display_infor()
        else:
            index = self.fileName[-5]
            num = str(int(index) - 1)
            self.fileName = self.replace_char(name, num, -5)
            self.mediaList = QMediaPlaylist()
            self.mediaList.addMedia(QMediaContent(QUrl(self.fileName)))
            self.player.setPlaylist(self.mediaList)
            self.mediaList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            self.player.play()  # 播放视频
            self.Process_ran()
            self.display_infor()

    def strTimeProp(self, start, end, prop, frmt):
        stime = time.mktime(time.strptime(start, frmt))
        etime = time.mktime(time.strptime(end, frmt))
        ptime = stime + prop * (etime - stime)
        return int(ptime)

    def randomDate(self, start, end, frmt='%Y-%m-%d'):
        return time.strftime(frmt, time.localtime(self.strTimeProp(start, end, random.random(), frmt)))

    def openVideoFile(self):
        self.output_class_9.setText('')
        self.output_class_10.setText('')
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self, 'Choose file', '', r'*.avi')
        self.mediaList = QMediaPlaylist()
        self.mediaList.addMedia(QMediaContent(QUrl(self.fileName)))
        self.player.setPlaylist(self.mediaList)
        self.mediaList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.label_51.clear()
        self.label_52.clear()
        self.wgt_video.raise_()
        self.player.play()  # 播放视频
        self.Process_ran()
        self.display_infor()

    def display_infor(self):
        x = xlrd.open_workbook(r"D:/Python/Projects/pyqt5_v1/ucf101_info.xlsx")
        sheet = x.sheet_by_name("Sheet1")
        if self.fileName == r"D:/Python/Projects/FIN/UCF-101/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01.avi":
            loader = str("@" + (sheet.col_values(2, 0, 1)[0]))
            self.output_class_25.setText(loader)
            name_1 = self.fileName[31:]
            str_0 = '/'
            name_2 = name_1[(name_1.index(str_0) + 1):]
            name_3 = name_2[2:]
            New_name = name_3[:-4]
            self.output_class_26.setText(New_name)
            self.label_8.setIcon(qtawesome.icon('fa.thumbs-o-up', color='black'))
            self.label_8.setIconSize(QtCore.QSize(30, 30))
            self.label_9.setIcon(qtawesome.icon('fa.commenting-o', color='black'))
            self.label_9.setIconSize(QtCore.QSize(30, 30))
            self.label_10.setIcon(qtawesome.icon('fa.share-alt', color='black'))
            self.label_10.setIconSize(QtCore.QSize(30, 30))
            date = '2008-01-01'
            self.output_class_27.setText(date)
        else:
            num = random.randint(0, 100)
            loader = str("@" + (sheet.col_values(2, num, num + 1)[0]))
            self.output_class_25.setText(loader)
            name_1 = self.fileName[31:]
            str_0 = '/'
            name_2 = name_1[(name_1.index(str_0) + 1):]
            name_3 = name_2[2:]
            New_name = name_3[:-4]
            self.output_class_26.setText(New_name)
            self.label_8.setIcon(qtawesome.icon('fa.thumbs-o-up', color='black'))
            self.label_8.setIconSize(QtCore.QSize(30, 30))
            self.label_9.setIcon(qtawesome.icon('fa.commenting-o', color='black'))
            self.label_9.setIconSize(QtCore.QSize(30, 30))
            self.label_10.setIcon(qtawesome.icon('fa.share-square-o', color='black'))
            self.label_10.setIconSize(QtCore.QSize(30, 30))
            date = self.randomDate('2008-01-01', '2019-01-01')
            self.output_class_27.setText(date)

    def Open_url(self):
        webbrowser.open('https://www.iti-tju.org/#/', new=1, autoraise=True)

    def Process_ran(self):  #点赞评论转发
        if self.fileName == r"D:/Python/Projects/FIN/UCF-101/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01.avi":
            self.output_class_14.setText(str(4320))
            self.output_class_15.setText(str(1500))
            self.output_class_16.setText(str(200))
        else:
            self.output_class_14.setText(str(random.randint(2000, 10000)))
            self.output_class_15.setText(str(random.randint(50, 2000)))
            self.output_class_16.setText(str(random.randint(0, 500)))

    def method(self):  #播放暂停
        if self.pushButton_35.text() == " ":
            self.playVideo()
            self.pushButton_35.setIcon(qtawesome.icon('fa.pause', color='#F76677', font=18))
            self.pushButton_35.setText("  ")
        elif self.pushButton_35.text() == "  ":
            self.pauseVideo()
            self.pushButton_35.setIcon(qtawesome.icon('fa.play', color='#F76677', font=18))
            self.pushButton_35.setText(" ")

    def playVideo(self):
        self.player.play()
    def pauseVideo(self):
        self.player.pause()
    def Accuracy(self):
        self.groupBox.raise_()
        self.widget_14.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.label_31.raise_()
    def ROC(self):
        self.groupBox.raise_()
        self.widget_14.raise_()
        self.label_33.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
    def FV(self):
        self.groupBox.raise_()
        self.widget_14.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
    def Return(self):
        self.groupBox.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.widget_14.raise_()
    def changeSlide(self,position):
        self.vidoeLength = self.player.duration()+0.1
        self.progressBar.setValue(round((position/self.vidoeLength)*100))
    def videoDoubleClicked(self,text):
        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                self.player.pause()
                self.videoFullScreenWidget.hide()
                self.player.setVideoOutput(self.wgt_video)
                self.player.play()
                self.videoFullScreen = False
            else:
                self.player.pause()
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.player.play()
                self.videoFullScreen = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    #gui=DanmuWindow(vieo_gui)
    vieo_gui.show()
    sys.exit(app.exec_())