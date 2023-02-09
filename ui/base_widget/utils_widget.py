# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, QEvent
from PyQt5.QtGui import *
from ui.base_widget.utlis_func import *

class buildCardBase(QWidget):
    def __init__(self,width, height):
        super().__init__()
        self.setFixedSize(SetWidthToScreen(width), SetHeightToScreen(height))
        self.setStyleSheet(
            "background-color: black;"
            "border: 2px solid #3399ff;"
            "border-radius: 20px")
        self.uiComponents()
    def uiComponents(self):
        column01 = QVBoxLayout()

        self.setLayout(column01)

class buildDivider(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(2)
        self.setObjectName('divider')
        self.setText('')
        self.setStyleSheet(f'''
        QWidget#divider {{
            background-color: white;
            border: 2px solid #3399ff;
        }}''')

class buildCardItem(QWidget):
    width = 0
    height = 0
    text = ''
    def __init__(self, text, width = 700, height = 80):
        super().__init__()
        self.text = text
        self.width = SetWidthToScreen(width)
        self.height = SetHeightToScreen(height)
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet(
            "background-color: #474747;"
            "border: none;"
            "border-radius: 10px;"
            "color: white;")
        self.components()
    
    def components(self):
        column = QVBoxLayout()
        column.setAlignment(Qt.AlignLeft)
        label = QLabel(self.text)
        label.setContentsMargins(12,0,12,0)
        label.setFont(QFont('Arial', SetRateToScreen(20)))
        column.addWidget(label)
        self.setLayout(column)
        self.setFixedSize(self.width, self.height)
        
class buildInputForm(QWidget):
    def __init__(self, width = 400, height = 80, isValidate = True):
        self.width = SetWidthToScreen(width)
        self.height = SetHeightToScreen(height)
        self.isValidate = isValidate
        super().__init__()
        self.setObjectName('buildInputForm')
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet(f'''
            QWidget {{
                background-color: white;
                border: none;
                border-radius: 10px;
                color: black;
            }}
            QWidget:focus {{
                background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #45ed80, stop: 1 #39e374);
                border: none;
                border-radius: 10px;
                color: black;
            }}
            ''')
        self.components()
    def components(self):
        self.column = QVBoxLayout()
        self.column.setAlignment(Qt.AlignVCenter)

        self.input = QLineEdit()
        if self.isValidate == True:
            self.input.setValidator(QIntValidator())
        self.input.setFixedSize(self.width-10, self.height-20)
        self.input.setFont(QFont('Arial', SetRateToScreen(20)))
        self.column.addWidget(self.input)

        self.setLayout(self.column)
    def event(self, event):
        if event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                self.focusNextPrevChild(True)
            if event.key() == Qt.Key_Escape:
                self.input.focusPreviousChild()
            if event.key() == Qt.Key_Shift:
                self.input.selectAll()
        # if event.type() == QEvent.MouseButtonPress :
        #     if event.button() == Qt.LeftButton:
        #         self.input.selectAll()
        # if event.type() == QEvent.FocusIn:
        #     self.setStyleSheet(
        #     "background-color: blue;"
        #     "border: none;"
        #     "border-radius: 10px;")
        return super().event(event)

class buildButton(QPushButton):
    def __init__(self,text, width, height):
        super().__init__()
        self.setFixedSize(SetWidthToScreen(width), SetHeightToScreen(height))
        self.setObjectName('buildButton')
        self.setText(text)
        self.setStyleSheet(
            "background-color: #d2eef4;"
            "border: none;"
            "border-radius: 10px;"
            "color: #1d212d")
        self.setFont(QFont("Arial", SetRateToScreen(20)))

class buildLabel(QLabel):
    def __init__(self, text, height = 100, fontSize = 20):
        super().__init__()
        self.setText(text)
        self.setFixedHeight(SetHeightToScreen(height))
        self.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.setFont(QFont("Arial", SetRateToScreen(fontSize)))

class Message(QWidget):
    def __init__(self, title, message, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setStyleSheet(
            "font-family: 'Roboto', sans-serif; font-size: 14px; font-weight: bold; padding: 0;")
        self.messageLabel = QLabel(message, self)
        self.messageLabel.setStyleSheet(
            "font-family: 'Roboto', sans-serif; font-size: 12px; font-weight: normal; padding: 0;")
        self.buttonClose = QPushButton(self)
        self.buttonClose.setIcon(QIcon("res/close1.png"))
        self.buttonClose.setFixedSize(14, 14)
        self.layout().addWidget(self.titleLabel, 0, 0)
        self.layout().addWidget(self.messageLabel, 1, 0)
        self.layout().addWidget(self.buttonClose, 0, 1, 2, 1)

class Notification(QWidget):
    # signNotifyClose = pyqtSignal(str)
    def __init__(self, parent = None):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "
        super(QWidget, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        resolution = QDesktopWidget().screenGeometry(-1)
        screenWidth = QDesktopWidget().width*0.5
        screenHeight = QDesktopWidget().height*0.5
        print(self.LOG_TAG + "width: " + str(resolution.width()) + " height: " + str(resolution.height()))
        self.nMessages = 0
        self.mainLayout = QVBoxLayout(self)
        self.move(screenWidth, screenHeight)

    def setNotify(self, title, message):
        m = Message(title, message, self)
        self.mainLayout.addWidget(m)
        m.buttonClose.clicked.connect(self.onClicked)
        self.nMessages += 1
        self.show()

    def onClicked(self):
        self.mainLayout.removeWidget(self.sender().parent())
        self.sender().parent().deleteLater()
        self.nMessages -= 1
        self.adjustSize()
        if self.nMessages == 0:
            self.close()

    
# Item Utils

class sizedBox10(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(10)
        self.setObjectName('sizedBox10')
        self.setStyleSheet(
            "background-color: transparent;"
            "border: none;"
            "border-radius: 10px;"
            "color: #1d212d")


