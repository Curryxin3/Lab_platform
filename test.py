# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from myVideoWidget import myVideoWidget
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QFont
import qtawesome
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from danmu import DanmuWindow

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.n=1
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(1142, 781)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1142, 781))

        self.setWindowOpacity(1)  # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 201, 781))
        self.widget.setStyleSheet('''
            QPushButton{border:none;color:white;font-size:16px}

            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-size:16px;font-weight:700;}

            QPushButton#left_button1:hover{border-left:5px solid red;font-size:20px;font-weight:800;}
            QPushButton#left_button2:hover{border-left:5px solid red;font-size:20px;font-weight:800;}

            QWidget#widget{
                background:#0d466c;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')
        self.widget.setObjectName("widget")
        self.pushButton_30 = QtWidgets.QPushButton(self.widget)     #依次为绿黄红按钮
        self.pushButton_30.setGeometry(QtCore.QRect(130, 10, 40, 30))
        self.pushButton_30.setText("")
        self.pushButton_30.setFixedSize(20,20)
        self.pushButton_30.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.widget)
        self.pushButton_31.setGeometry(QtCore.QRect(80, 10, 40, 30))
        self.pushButton_31.setText("")
        self.pushButton_31.setFixedSize(20,20)
        self.pushButton_31.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.widget)
        self.pushButton_32.setGeometry(QtCore.QRect(30, 10, 40, 30))
        self.pushButton_32.setText("")
        self.pushButton_32.setFixedSize(20,20)
        self.pushButton_32.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton_32.setObjectName("pushButton_32")

        self.pushButton_11 = QtWidgets.QPushButton(qtawesome.icon('fa.file-video-o',color='white'),"File",self.widget)  #打开文件
        self.pushButton_11.setGeometry(QtCore.QRect(10, 60, 90, 41))
        self.pushButton_11.setStyleSheet("font: 10pt \"黑体\";")
        self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_11.setObjectName("left_button1")
        self.pushButton_52 = QtWidgets.QPushButton(qtawesome.icon('fa.file-video-o',color='white'),"Camera",self.widget)  #打开摄像头
        self.pushButton_52.setGeometry(QtCore.QRect(101, 60, 90, 41))
        self.pushButton_52.setStyleSheet("font: 10pt \"黑体\";")
        self.pushButton_52.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_52.setObjectName("left_button2")

        self.pushButton_24 = QtWidgets.QPushButton("功能列表",self.widget)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 120, 181, 41))
        self.pushButton_24.setObjectName("left_label")
        self.pushButton_7 = QtWidgets.QPushButton(qtawesome.icon('fa.building',color='white'),"场景估计",self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 200, 161, 30))
        self.pushButton_7.setObjectName("left_button")
        self.pushButton_8 = QtWidgets.QPushButton(qtawesome.icon('fa.male',color='white'),"事件检测",self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 260, 161, 31))
        self.pushButton_8.setObjectName("left_button")
        self.pushButton_25 = QtWidgets.QPushButton(qtawesome.icon('fa.smile-o',color='white'),"情感分析",self.widget)
        self.pushButton_25.setGeometry(QtCore.QRect(20, 320, 161, 31))
        self.pushButton_25.setObjectName("left_button")
        self.pushButton_10 = QtWidgets.QPushButton(qtawesome.icon('fa.female',color='white'),"时尚分析",self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 380, 161, 31))
        self.pushButton_10.setObjectName("left_button")
        self.pushButton_9 = QtWidgets.QPushButton(qtawesome.icon('fa.share-square',color='white'),"流行度预测",self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 440, 161, 30))
        self.pushButton_9.setObjectName("left_button")
        self.pushButton_36 = QtWidgets.QPushButton(qtawesome.icon('fa.eye',color='white'),"记忆度分析",self.widget)
        self.pushButton_36.setGeometry(QtCore.QRect(20, 500, 161, 31))
        self.pushButton_36.setObjectName("left_button")
        self.pushButton_29 = QtWidgets.QPushButton("联系与帮助",self.widget)
        self.pushButton_29.setGeometry(QtCore.QRect(10, 550, 181, 40))
        self.pushButton_29.setObjectName("left_label")
        self.pushButton_26 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"关注我们",self.widget)
        self.pushButton_26.setGeometry(QtCore.QRect(20, 610, 161, 30))
        self.pushButton_26.setObjectName("left_button")
        self.pushButton_27 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题",self.widget)
        self.pushButton_27.setGeometry(QtCore.QRect(20, 670, 161, 30))
        self.pushButton_27.setObjectName("left_button")
        self.pushButton_28 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"反馈建议",self.widget)
        self.pushButton_28.setGeometry(QtCore.QRect(20, 730, 161, 30))
        self.pushButton_28.setObjectName("left_button")

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)    #整个右半部分
        self.widget_2.setGeometry(QtCore.QRect(200, 0, 941, 781))
        self.widget_2.setStyleSheet('''
            QWidget#widget_2{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
        ''')
        self.widget_2.setObjectName("widget_2")

        self.widget_6 = QtWidgets.QWidget(self.widget_2)    #顶部左侧
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 550, 72))
        self.widget_6.setStyleSheet('''
            QWidget#widget_6{
                background:#d7d7d7;
            }
        ''')
        self.widget_6.setObjectName("widget_6")
        self.label_2 = QtWidgets.QLabel(self.widget_6)   #天大图标
        self.label_2.setGeometry(QtCore.QRect(15, 3, 72, 65))
        self.label_2.setStyleSheet("border-image: url(:/2/PIC/4.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_32 = QtWidgets.QPushButton("  天津大学电视图像信息研究所", self.widget_6)
        self.pushButton_32.setGeometry(QtCore.QRect(105, 12, 380, 25))
        self.pushButton_32.setStyleSheet("color: rgb(27, 68, 95);font: 14pt;border:none;font-weight:bold;")
        self.pushButton_32.setFont(QFont("幼圆"))
        self.pushButton_32.setObjectName("push_32")
        self.pushButton_33 = QtWidgets.QPushButton("Institute of Television and Image Information,Ministry of Education", self.widget_6)
        self.pushButton_33.setGeometry(QtCore.QRect(98, 42, 450, 21))
        self.pushButton_33.setStyleSheet("color: rgb(27, 68, 95);font: 9pt;border:none;")
        self.pushButton_33.setFont(QFont("Roman times"))
        self.pushButton_33.setObjectName("push_32")

        self.widget_3 = QtWidgets.QWidget(self.widget_2)   #顶部右侧
        self.widget_3.setGeometry(QtCore.QRect(500, 0, 490, 72))
        self.widget_3.setStyleSheet('''
             QPushButton{color: rgb(27, 68, 95);font: 14pt;border:none;font-weight:bold;}
             QPushButton#w3_button:hover{border-bottom:3px solid #0d466c;font-weight:700;}
             QWidget#widget_3{
                 background:#d7d7d7;
                 border-top-right-radius:10px;
             }
         ''')
        self.widget_3.setObjectName("widget_3")
        self.pushButton_18 = QtWidgets.QPushButton("主页", self.widget_3)
        self.pushButton_18.setGeometry(QtCore.QRect(100, 23, 50, 30))
        self.pushButton_18.setObjectName("w3_button")
        self.pushButton_20 = QtWidgets.QPushButton("团队", self.widget_3)
        self.pushButton_20.setGeometry(QtCore.QRect(160, 23, 61, 31))
        self.pushButton_20.setObjectName("w3_button")
        self.pushButton_21 = QtWidgets.QPushButton("研究方向", self.widget_3)
        self.pushButton_21.setGeometry(QtCore.QRect(230, 23, 111, 31))
        self.pushButton_21.setObjectName("w3_button")
        self.pushButton_22 = QtWidgets.QPushButton("联系", self.widget_3)
        self.pushButton_22.setGeometry(QtCore.QRect(350, 23, 61, 31))
        self.pushButton_22.setObjectName("w3_button")

        self.pm = QPixmap("./img/a" +str(1)+".jpg")
        self.label_20 = QLabel(self.widget_2)    #滚动播放
        self.label_20.setPixmap(self.pm)
        self.label_20.setGeometry(QtCore.QRect(0, 72, 941, 215))
        self.label_20.setScaledContents(True)
        timer1=QTimer(self)
        timer1.timeout.connect(self.timer_TimeOut)
        timer1.start(2000)
        self.show()

        self.label = QtWidgets.QLabel(chr(0xf002) + ' '+'搜索  ',self.widget_2)  #搜索框
        self.label.setGeometry(QtCore.QRect(20, 295, 100, 30))
        self.label.setFont(qtawesome.font('fa', 18))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setPlaceholderText("输入视频或用户，回车进行搜索")
        self.lineEdit.setGeometry(QtCore.QRect(85, 298, 336, 22))
        self.lineEdit.setStyleSheet('''QLineEdit{
                border:1px solid #444444;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(chr(0xf03d)+'\n'+'视\n频\n播\n放',self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(17,325, 41, 170))
        self.label_3.setStyleSheet("color: #282828;font: 18pt;border:none;font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(qtawesome.font('fa', 16))

        self.widget_4 = QtWidgets.QWidget(self.widget_2)   #整个视频播放区
        self.widget_4.setGeometry(QtCore.QRect(70, 330, 350, 380))
        self.widget_4.setStyleSheet('''
              QWidget#widget_4{
                  color:#232C51;
                  background:white;
                  border-top:2px solid #444444;
                  border-bottom:2px solid #444444;
                  border-right:2px solid #444444;
                  border-left:2px solid #444444;
                  border-top-right-radius:10px;
                  border-bottom-right-radius:10px;
                  border-top-left-radius:10px;
                  border-bottom-left-radius:10px;
              }
         ''')
        self.widget_4.setObjectName("widget_4")
        self.wgt_video = myVideoWidget(self.widget_2)   #播放视频窗口
        self.wgt_video.setGeometry(QtCore.QRect(75, 335, 340, 280))
        self.wgt_video.setObjectName("wgt_video")
        self.label_51 = QtWidgets.QLabel(self.widget_2)   #情感中的文件窗口
        self.label_51.setGeometry(QtCore.QRect(75, 346, 340, 260))
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.widget_2)   #情感中的摄像头窗口
        self.label_52.setGeometry(QtCore.QRect(75, 310, 360, 420))
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")

        self.widget_8 = QtWidgets.QWidget(self.widget_4)   #信息窗口
        self.widget_8.setGeometry(QtCore.QRect(2, 284, 346, 60))
        self.widget_8.setStyleSheet('''
                   QWidget#widget_8{
                       background:white;
                       border-bottom-right-radius:10px;
                       border-bottom-left-radius:10px;
                   }
               ''')
        self.widget_8.setObjectName("widget_8")
        self.output_class_25 = QtWidgets.QLineEdit(self.widget_8)
        self.output_class_25.setGeometry(QtCore.QRect(10, 0, 170, 30))
        self.output_class_25.setStyleSheet('''
                 font-size:20px;
                 font-weight:bold;
                 color:black;
                 border:none;
        ''')
        self.output_class_25.setFont(QFont("幼圆"))
        self.output_class_25.setText("")
        self.output_class_25.setObjectName("output_class_25")
        self.output_class_27 = QtWidgets.QLineEdit(self.widget_8)
        self.output_class_27.setGeometry(QtCore.QRect(180, 0, 170, 30))
        self.output_class_27.setStyleSheet('''
                  font-size:20px;
                  font-weight:bold;
                  color:black;
                  border:none;

         ''')
        self.output_class_27.setText("")
        self.output_class_27.setFont(QFont("幼圆"))
        self.output_class_27.setObjectName("output_class_27")
        self.output_class_26 = QtWidgets.QLineEdit(self.widget_8)
        self.output_class_26.setGeometry(QtCore.QRect(10, 30, 346, 30))
        self.output_class_26.setStyleSheet('''
                 font-size:16px;
                 color:black;
                 border:none;
                 background:white;

        ''')
        self.output_class_26.setText("")
        self.output_class_26.setObjectName("output_class_26")

        self.widget_7 = QtWidgets.QWidget(self.widget_4)    #点赞评论转发窗口
        self.widget_7.setGeometry(QtCore.QRect(2, 340, 346, 30))
        self.widget_7.setStyleSheet('''
            QWidget#widget_7{
                background:white;
                border-top-right-radius:10px;
            }
            Qlabel#w7label{background: white;}
            QLineEdit#w7Line{
                border:none;
            }
        ''')
        self.widget_7.setObjectName("widget_7")
        self.label_8 = QtWidgets.QPushButton(self.widget_7)
        self.label_8.setGeometry(QtCore.QRect(15, 5, 30, 30))
        self.label_8.setFont(qtawesome.font('fa', 27))
        self.label_8.setStyleSheet("color:black;border:none;")
        self.label_8.setObjectName("w7label")
        self.label_9 = QtWidgets.QPushButton(self.widget_7)
        self.label_9.setGeometry(QtCore.QRect(95, 5, 30, 30))
        self.label_9.setFont(qtawesome.font('fa', 27))
        self.label_9.setStyleSheet("color:black;border:none;")
        self.label_9.setObjectName("w7label")
        self.label_10 = QtWidgets.QPushButton(self.widget_7)
        self.label_10.setGeometry(QtCore.QRect(180, 5, 30, 30))
        self.label_10.setFont(qtawesome.font('fa', 27))
        self.label_10.setStyleSheet("color:black;border:none;")
        self.label_10.setObjectName("w7label")
        self.output_class_14 = QtWidgets.QLineEdit(self.widget_7)
        self.output_class_14.setAlignment(QtCore.Qt.AlignCenter)
        self.output_class_14.setGeometry(QtCore.QRect(42, 0, 50, 40))
        self.output_class_14.setStyleSheet("font: 10pt;background:white;color:black")
        self.output_class_14.setText(" ")
        self.output_class_14.setFont(QFont("幼圆"))
        self.output_class_14.setObjectName("w7Line")
        self.output_class_15 = QtWidgets.QLineEdit(self.widget_7)
        self.output_class_15.setAlignment(QtCore.Qt.AlignCenter)
        self.output_class_15.setGeometry(QtCore.QRect(127, 0, 50, 40))
        self.output_class_15.setStyleSheet("font: 10pt;background:white;color:black")
        self.output_class_15.setText("")
        self.output_class_15.setObjectName("w7Line")
        self.output_class_15.setFont(QFont("幼圆"))
        self.output_class_16 = QtWidgets.QLineEdit(self.widget_7)
        self.output_class_16.setAlignment(QtCore.Qt.AlignCenter)
        self.output_class_16.setGeometry(QtCore.QRect(207,0, 50, 40))
        self.output_class_16.setStyleSheet("font: 10pt;background:white;color:black")
        self.output_class_16.setText("")
        self.output_class_16.setFont(QFont("幼圆"))
        self.output_class_16.setObjectName("w7Line")

        self.label_4 = QtWidgets.QLabel(chr(0xf19d)+'\n多\n媒\n体\n计\n算',self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(450, 290, 40, 200))
        self.label_4.setStyleSheet("color: #282828;font: 18pt;border:none;font-weight:bold;")
        self.label_4.setFont(QFont("幼圆"))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(qtawesome.font('fa', 16))

        self.widget_9 = QtWidgets.QWidget(self.widget_2)    #结果窗口
        self.widget_9.setGeometry(QtCore.QRect(500, 295, 405, 160))
        self.widget_9.setStyleSheet('''
                   QWidget#widget_9{
                       background:white;
                       border:none;
                   }
               ''')
        self.widget_9.setObjectName("widget_9")

        self.comboBox1 = QtWidgets.QComboBox(self.widget_9)
        self.comboBox1.setGeometry(QtCore.QRect(30, 7, 120, 35))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("场景估计")
        self.comboBox1.addItem("事件检测")
        self.comboBox1.addItem("时尚分析")
        self.comboBox1.addItem("情感分析")
        self.comboBox1.addItem("流行度分析")
        self.comboBox1.addItem("记忆度分析")
        self.comboBox1.setStyleSheet("QComboBox{background:white;}")
        self.comboBox = QtWidgets.QComboBox(self.widget_9)
        self.comboBox.setGeometry(QtCore.QRect(190, 7, 120, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("C3D")
        self.comboBox.addItem("modelA")
        self.comboBox.addItem("modelB")
        self.comboBox.addItem("modelC")
        self.comboBox.addItem("modelD")
        self.comboBox.setStyleSheet("QComboBox{background:white}")
        self.pushButton_34 = QtWidgets.QPushButton(qtawesome.icon('fa.play-circle-o', color='#1b445f'), "",self.widget_9)
        self.pushButton_34.setGeometry(QtCore.QRect(340, 3, 40, 40))
        self.pushButton_34.setText("")
        self.pushButton_34.setIconSize(QtCore.QSize(40,40))
        self.pushButton_34.setStyleSheet('''QPushButton{background:white;border-radius:20px;border:none}QPushButton:hover{background:green;}''')
        self.pushButton_34.setObjectName("pushButton_34")
        self.lineEdit_2 = QtWidgets.QLineEdit("RESULT",self.widget_9)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 55, 260, 50))
        self.lineEdit_2.setStyleSheet('''
                 color:#232C51;
                 border:none;
                 background:white;
                 border-top:2px solid #444444;
                 border-bottom:2px solid #444444;
                 border-right:2px solid #444444;
                 border-left:2px solid #444444;
                 border-top-left-radius:10px;
                 font-size:20px;
        ''')

        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit("  Accuracy",self.widget_9)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 55, 115, 50))
        self.lineEdit_4.setStyleSheet('''
                 color:#232C51;
                 border:none;
                 background:white;
                 border-top:2px solid #444444;
                 border-bottom:2px solid #444444;
                 border-right:2px solid #444444;
                 border-top-right-radius:10px;
                 font-size:20px
        ''')
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.output_class_9 = QtWidgets.QLineEdit(self.widget_9)
        self.output_class_9.setAlignment(QtCore.Qt.AlignCenter)
        self.output_class_9.setGeometry(QtCore.QRect(10, 105, 260, 50))
        self.output_class_9.setStyleSheet('''
                 font-size:20px;
                 color:#232C51;
                 border:none;
                 background:white;
                 border-bottom:2px solid #444444;
                 border-right:2px solid #444444;
                 border-left:2px solid #444444;
                 border-bottom-left-radius:10px;
        ''')
        self.output_class_9.setText("")
        self.output_class_9.setObjectName("output_class_9")
        self.output_class_10 = QtWidgets.QLineEdit(self.widget_9)
        self.output_class_10.setAlignment(QtCore.Qt.AlignCenter)
        self.output_class_10.setGeometry(QtCore.QRect(270, 105, 115, 50))
        self.output_class_10.setStyleSheet('''
                 font-size:20px;
                 color:#232C51;
                 border:none;
                 background:white;
                 border-bottom:2px solid #444444;
                 border-right:2px solid #444444;
                 border-bottom-right-radius:10px;
        ''')
        self.output_class_10.setText("")
        self.output_class_10.setObjectName("output_class_10")

        self.groupBox = QtWidgets.QGroupBox("性能分析 ",self.widget_2)   #性能分析窗口
        self.groupBox.setGeometry(QtCore.QRect(510, 470, 380, 235))
        self.groupBox.setStyleSheet('''
            QGroupBox#groupBox{
                 color:#232C51;
                 border:2px solid #444444;
                 background:white;
                 margin-top:3px;
                 border-radius:10px;
                 font-size:16px;
                 }
            QGroupBox:title{
                 subcontrol-origin:margin;
                 subcontrol-position:top left;
                 left:8px;
                 color:blue;
                 }
        ''')
        self.groupBox.setObjectName("groupBox")

        self.pushButton_41 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart',color='#F8325d'),"",self.groupBox)
        self.pushButton_41.setGeometry(QtCore.QRect(15, 22, 40, 40))
        self.pushButton_41.setText("")
        self.pushButton_41.setIconSize(QtCore.QSize(32,32))
        self.pushButton_41.setStyleSheet('''QPushButton{border:none}QPushButton:hover{background:red;}''')
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_41 = QtWidgets.QLabel("Accuracy",self.groupBox)
        self.label_41.setGeometry(QtCore.QRect(6, 45, 65, 40))
        self.label_41.setStyleSheet("color:'#F8325D' ;font: 9pt;border:none;")
        self.label_41.setFont(QFont("幼圆"))
        self.label_41.setObjectName("label_41")
        self.pushButton_42 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart',color='#b6b600'),"",self.groupBox)
        self.pushButton_42.setGeometry(QtCore.QRect(15, 75, 40, 40))
        self.pushButton_42.setText("")
        self.pushButton_42.setIconSize(QtCore.QSize(32,32))
        self.pushButton_42.setStyleSheet('''QPushButton{border:none}QPushButton:hover{background:yellow;}''')
        self.pushButton_42.setObjectName("pushButton_42")
        self.label_42 = QtWidgets.QLabel("  ROC",self.groupBox)
        self.label_42.setGeometry(QtCore.QRect(6, 98, 65, 40))
        self.label_42.setStyleSheet("color:'#b6b600' ;font: 10pt;border:none;")
        self.label_42.setFont(QFont("幼圆"))
        self.label_42.setObjectName("label_42")
        self.pushButton_43 = QtWidgets.QPushButton(qtawesome.icon('fa.pie-chart',color='#009900'),"",self.groupBox)
        self.pushButton_43.setGeometry(QtCore.QRect(15, 130, 40, 40))
        self.pushButton_43.setText("")
        self.pushButton_43.setIconSize(QtCore.QSize(32,32))
        self.pushButton_43.setStyleSheet('''QPushButton{border:none}QPushButton:hover{background:green;}''')
        self.pushButton_43.setObjectName("pushButton_43")
        self.label_43 = QtWidgets.QLabel("visualize",self.groupBox)
        self.label_43.setGeometry(QtCore.QRect(6, 150, 75, 40))
        self.label_43.setStyleSheet("color:'#009900' ;font: 10pt;border:none;")
        self.label_43.setFont(QFont("幼圆"))
        self.label_43.setObjectName("label_43")
        self.pushButton_44 = QtWidgets.QPushButton(qtawesome.icon('fa.share',color='#0d466c'),"",self.groupBox)
        self.pushButton_44.setGeometry(QtCore.QRect(15, 180, 40, 40))
        self.pushButton_44.setText("")
        self.pushButton_44.setIconSize(QtCore.QSize(32,32))
        self.pushButton_44.setStyleSheet('''QPushButton{border:none}QPushButton:hover{background:blue;}''')
        self.pushButton_44.setObjectName("pushButton_43")
        self.label_44 = QtWidgets.QLabel("Return",self.groupBox)
        self.label_44.setGeometry(QtCore.QRect(6, 200, 75, 40))
        self.label_44.setStyleSheet("color:'#0d466c';font: 10pt;border:none;")
        self.label_44.setFont(QFont("幼圆"))
        self.label_44.setObjectName("label_44")
        self.widget_14 = QtWidgets.QWidget(self.groupBox)
        self.widget_14.setGeometry(QtCore.QRect(80, 10, 260, 205))
        self.widget_14.setStyleSheet('''
                   QWidget#widget_14{
                       background:white;
                       border:none;
                   }
               ''')
        self.widget_14.setObjectName("widget_14")
        self.danmu = DanmuWindow(self.widget_14)
        self.danmu.setGeometry(5,10,290,200)
        self.danmu.setObjectName("dammu")
        self.pm31 = QPixmap("D:/Python/Projects/pyqt5_V4.0/pyqt5_V4.0/img/A"+".jpg")
        self.label_31 = QLabel(self.groupBox)
        self.label_31.setPixmap(self.pm31)
        self.label_31.setGeometry(QtCore.QRect(80, 10, 260, 205))
        self.label_31.setScaledContents(True)
        self.pm32 = QPixmap("./img/R"+".jpg")
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setPixmap(self.pm32)
        self.label_32.setGeometry(QtCore.QRect(80, 10, 260, 205))
        self.label_32.setScaledContents(True)
        self.pm33 = QPixmap("./img/F"+".jpg")
        self.label_33 = QLabel(self.groupBox)
        self.label_33.setPixmap(self.pm33)
        self.label_33.setGeometry(QtCore.QRect(80, 10, 260, 205))
        self.label_33.setScaledContents(True)
        self.groupBox.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.widget_14.raise_()

        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(50, 730, 855, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setMaximum(100)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setFixedHeight(5)  # 设置进度条高度
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')
        self.progressBar.setObjectName("progressBar")   #视频播放暂停窗口
        self.pushButton_33 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "",self.widget_2)
        self.pushButton_33.setGeometry(QtCore.QRect(405, 740, 30, 30))
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_33.setIconSize(QtCore.QSize(20,20))
        self.pushButton_33.setStyleSheet("border:none;")
        self.pushButton_35 = QtWidgets.QPushButton(qtawesome.icon('fa.pause', color='#F76677', font=18), " ",self.widget_2)
        self.pushButton_35.setGeometry(QtCore.QRect(436, 735, 48, 40))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_35.setStyleSheet("border:none;")
        self.pushButton_35.setIconSize(QtCore.QSize(20,30))
        self.pushButton_23 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "",self.widget_2)
        self.pushButton_23.setGeometry(QtCore.QRect(485, 740, 30, 30))
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.setStyleSheet("border:none;")
        self.pushButton_23.setIconSize(QtCore.QSize(20, 20))

        self.setCentralWidget(self.centralwidget)

    def timer_TimeOut(self):
        self.n+=1
        if self.n>2:
            self.n=1
        self.pm = QPixmap("./img/a" + str(self.n) + ".jpg")
        self.label_20.setPixmap(self.pm)
import test_rc
