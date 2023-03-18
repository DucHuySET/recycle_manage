# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from app_ui.base_widget.utils_widget import *
from app_ui.base_widget.utlis_func import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1d212d")
        self.exportId = 0
        self.uiComponents()
        self.show()
    def uiComponents(self):
        #creating Column
        self.column = QVBoxLayout()
        self.column.setAlignment(Qt.AlignCenter)
        self.column.setSpacing(SetHeightToScreen(100))

        self.label = QLabel("Quản lý nhập, xuất kho phế liệu")
        self.label.setStyleSheet("color: #d2eef4;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', SetRateToScreen(30), 1))
        self.column.addWidget(self.label)

        self.row = QHBoxLayout()
        self.row.setAlignment(Qt.AlignCenter)
        self.row.setSpacing(SetRateToScreen(50))
        self.column.addLayout(self.row)

        self.button_import = buildButton("Quản lý lượt cân \nđầu vào", SetWidthToScreen(300), SetHeightToScreen(200))
        self.row.addWidget(self.button_import)

        self.button_export = buildButton("Quản lý lượt cân \nđầu ra", SetWidthToScreen(300), SetHeightToScreen(200))
        self.row.addWidget(self.button_export)

        self.widget = QWidget()
        self.widget.setLayout(self.column)
        self.setCentralWidget(self.widget)
        # # opening window in maximized size
        self.showMaximized()
