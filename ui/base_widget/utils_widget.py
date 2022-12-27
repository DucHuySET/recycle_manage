# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, QEvent
from PyQt5.QtGui import QFont, QIcon

class buildCardBase(QWidget):
    def __init__(self,width, height):
        super().__init__()
        self.setFixedSize(width, height)
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
    def __init__(self,width, height, text):
        super().__init__()
        self.text = text
        self.width = width
        self.height = height
        self.setFixedSize(width, height)
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
        label.setFont(QFont('Arial', 20))
        column.addWidget(label)
        self.setLayout(column)
        self.setFixedSize(self.width, self.height)
        
class buildInputForm(QWidget):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()
        self.setObjectName('buildInputForm')
        self.setFixedSize(width, height)
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
        self.input.setFixedSize(self.width-10, self.height-20)
        self.input.setFont(QFont('Arial', 20))
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
        self.setFixedSize(width, height)
        self.setObjectName('buildButton')
        self.setText(text)
        self.setStyleSheet(
            "background-color: #d2eef4;"
            "border: none;"
            "border-radius: 10px;"
            "color: #1d212d")
        self.setFont(QFont("Arial", 20))

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


