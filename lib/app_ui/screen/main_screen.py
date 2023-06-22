# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from lib.app_ui.base_widget.utils_widget import *
from lib.core.utils_function.utlis_func import SetHeightToScreen, SetRateToScreen, SetWidthToScreen
from lib.core.values.strings import AppStr

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
        self.column.totalMaximumSize()

        self.verticalSpacerTop = QSpacerItem(10, SetHeightToScreen(350), QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.column.addSpacerItem(self.verticalSpacerTop)

        self.label = QLabel(AppStr.MAIN_SCREEN_LABEL)
        self.label.setStyleSheet("color: #d2eef4;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', SetRateToScreen(30), 1))
        self.column.addWidget(self.label)

        self.row = QHBoxLayout()
        self.row.setAlignment(Qt.AlignCenter)
        self.row.setSpacing(SetRateToScreen(50))
        self.row.totalMaximumSize()
        self.column.addLayout(self.row)

        self.verticalSpacerBottom = QSpacerItem(10, SetHeightToScreen(350), QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.column.addSpacerItem(self.verticalSpacerBottom)

        self.horizontalSpacerLeft = QSpacerItem(SetHeightToScreen(600), 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.row.addSpacerItem(self.horizontalSpacerLeft)

        self.button_import = buildButton("Quản lý lượt cân \nđầu vào")
        self.button_import.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.row.addWidget(self.button_import)

        self.button_export = buildButton("Quản lý lượt cân \nđầu ra",)
        self.button_export.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.row.addWidget(self.button_export)

        self.horizontalSpacerRight = QSpacerItem(SetHeightToScreen(600), 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.row.addSpacerItem(self.horizontalSpacerRight)

        self.widget = QWidget()
        self.widget.setLayout(self.column)
        self.setCentralWidget(self.widget)
        # # opening window in maximized size
        self.showMaximized()
