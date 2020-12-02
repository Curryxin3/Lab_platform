import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
from queue import Queue
import threading
import time


WORD_LIST = []
# TEXT_COLOR = ['#426F42', '#7F00FF', '#7FFF00', '#70DBDB', '#DB7093', '#A68064', '#2F2F4F', '#23238E',
#               '#4D4DFF', '#FF6EC7', '#00009C', '#EBC79E', '#CFB53B', '#FF7F00', '#FF2400', '#DB70DB'
TEXT_COLOR = ['#6DDF6D','#F7D674','#F76677']
LOOP_TIME = 20000
LOOP_COUNT = 100
circle_num = 0  ## 记录颜色


def load_word_file():
    yes = 0
    file = 'test.txt'
    if not os.path.exists(file):
        with open(file, 'w', encoding='utf8') as f:
            pass
    with open(file, 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                WORD_LIST.append(line)
    if WORD_LIST:
        yes = 1
    return yes


class Tip(QListWidget):
    # font = QFont('宋体', 5, 5)
    def __init__(self, list_text,list_text1,list_text2, parent=None,x=0, y=0):

        try:
            super().__init__( parent)
            self.setGeometry(x, y, 150, 70)
            self.addItem(list_text[0])
            self.addItem(list_text1[0])
            self.addItem(list_text2[0])
            # self.setFlow()
            # self.wordWrap(True)
            # self.setTextElideMode(Qt_TextElideMode=None)
            # # self.label_14 = QtWidgets.QLabel("学习率", self.widget_2)
            # self.label = QtWidgets.QLabel()
            # self.adjustSize()
            self.setStyleSheet(
                 "QListWidget{background-color: rgba(51, 62, 80, 0.8);border-radius:10px;color:rgb(189, 192, 197);font-size:14px;} " \
                 "QScrollBar:vertical{width:8px;background:rgba(51, 62, 80, 0.8); background-color:rgba(51, 62, 80, 0.8);}" \
                 "QScrollBar:horizontal{height:8px;background:rgba(51, 62, 80, 0.8);background-color:rgba(51, 62, 80, 0.8);}")
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        except Exception as e:
            print(str(e))


class DButton(QPushButton):
    font = QFont('宋体', 20, 40)
    _state = 0

    def __init__(self, parent, text, y=0, color=QColor(255, 255, 255)):
        cur_text = text.split(':')[0]
        super().__init__(cur_text, parent)
        self.text = cur_text
        # print(self.text)
        descript = text[(len(self.text)):]
        self.tip = descript.split(':')[1].split(',')
        des1 = descript[len(self.tip):]
        self.tip1 = des1.split(',')[1].split(';')
        des2 = des1[len(self.tip1):]
        self.tip2 =des2.split(';')[1].split('.')

        self.parent = parent
        self.setCursor(Qt.PointingHandCursor)
        self.setFont(self.font)
        self.setFixedHeight(50)
        self.setposY(y)
        self.adjustSize()  # 宽度自适应
        # text_color = random.sample(TEXT_COLOR,1)
        # text_color = TEXT_COLOR.split(',')[0]
        if self.text=='Accuracy':
            text_color=TEXT_COLOR[0]
        if self.text=='ROC':
            text_color=TEXT_COLOR[1]
        if self.text=='FV':
            text_color=TEXT_COLOR[2]
        style_sheet = "QPushButton{background-color: rgba(97%,80%,9%,1%);border:none;color:" + text_color+ "}"
        self.setStyleSheet(style_sheet)
        self.anim2 = QPropertyAnimation(self, b'pos')
        self.anim2.setDuration(LOOP_TIME)
        start = random.randint(0, 100)
        # window_width = QDesktopWidget().screenGeometry().width()
        window_width = 350
        self.anim2.setStartValue(QPoint(window_width - start, self.posY))

        self.anim2.setEndValue(QPoint(0, self.posY))
        self.anim2.setEasingCurve(QEasingCurve.Linear)
        self.anim2.finished.connect(self.end)
        if LOOP_COUNT:
            self.anim2.setLoopCount(LOOP_COUNT)
        self.anim2.start()

    def end(self):
        self.deleteLater()
        # self.parent.resume_move()
        self.parent = None
        self = None

    def enterEvent(self, event):
        if not self._state:
            self.anim2.pause()
            self.show_tips()

    def leaveEvent(self, event):
        # time.sleep(0.5)
        if not self._state:
            self.anim2.resume()
            self._tip.deleteLater()

    def mouseReleaseEvent(self, event):
        if not self._state:
            self._state = 1
        else:
            self._state = 0

    def show_tips(self):
        list_text = self.tip
        list_text1 =self.tip1
        list_text2 = self.tip2
        tip = Tip(list_text,list_text1, list_text2,self.parent, self.x() + self.width(), self.y())
        self._tip = tip
        self._tip.show()

    def setposY(self, y):
        self.posY = y

class DanmuWindow(QWidget):
    _signal = pyqtSignal(str)
    max_height = 0

    def __init__(self, parent=None):
        # def __init__(self, q=Queue(), parent=None):
        super(DanmuWindow, self).__init__(parent)
    # def __init__(self, q=Queue()):
    #     super().__init__()

        self._signal.connect(self.mySignal)
        # self.max_height = QDesktopWidget().screenGeometry().height() - 100

        # self.setGeometry(0, 0, QDesktopWidget().screenGeometry().width(),
        #                  self.max_height)
        # self.setGeometry(0,0,380,300)

        # self.q = q
        self.th = threading.Thread(target=self.start_move)
        self.th.setDaemon(True)  # 守护线程

        yes = load_word_file()
        if yes == 1:
            self.th.start()


    def mySignal(self, text):
        danmu = DButton(self, text, self.get_random_height(), QColor(255, 255, 255))
        danmu.show()

    def get_random_height(self):
        height = random.randint(20, 200)
        mod = height % 10
        if mod:
              height = height - mod

        return height

    def resume_move(self):
        pass
        # self.mySignal(WORD_LIST.pop(0))

    def start_move(self):
        while True:
            for i in range(1):
                if WORD_LIST:
                    self._signal.emit(WORD_LIST.pop(0))
            time.sleep(7)

import sys
if __name__ == '__main__':

      app = QApplication(sys.argv)
      vieo_gui = DanmuWindow()
      vieo_gui.show()
      sys.exit(app.exec_())