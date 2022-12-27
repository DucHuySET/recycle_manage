# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon
from ui.base_widget.utils_widget import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: #1d212d")
        self.uiComponents()
        self.show()
        self.exportId = 0
    def uiComponents(self):
        #creating Column
        self.column = QVBoxLayout()
        self.column.setAlignment(Qt.AlignCenter)
        self.column.setSpacing(100)

        self.label = QLabel("Quản lý nhập, xuất kho phế liệu")
        self.label.setStyleSheet("color: #d2eef4;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 30, 1))
        self.column.addWidget(self.label)

        self.row = QHBoxLayout()
        self.row.setAlignment(Qt.AlignCenter)
        self.row.setSpacing(50)
        self.column.addLayout(self.row)

        self.button_import = buildButton("Quản lý lượt cân \nđầu vào", 300, 200)
        self.row.addWidget(self.button_import)

        self.button_export = buildButton("Quản lý lượt cân \nđầu ra", 300, 200)
        self.row.addWidget(self.button_export)

        self.widget = QWidget()
        self.widget.setLayout(self.column)
        self.setCentralWidget(self.widget)
        # # opening window in maximized size
        self.showMaximized()
