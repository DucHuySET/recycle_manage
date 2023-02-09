# This Python file uses the following encoding: utf-8
import math
from PyQt5.QtWidgets import *

from core.values.strings import AppStr



def ShowNotification(title, message, funcYes):
    dialog = QMessageBox()
    dialog.setIcon(QMessageBox.Icon.Critical)
    dialog.setWindowTitle(title)
    dialog.setText(message)
    yesButton = QPushButton(AppStr.CONTINUE)
    noButton = QPushButton(AppStr.CANCEL)
    # dialog.addButton(yesButton, QMessageBox().YesRole)
    dialog.addButton(noButton, QMessageBox().NoRole)
    dialog.setDefaultButton(noButton)
    dialog.exec()

    # if dialog.clickedButton() != dialog.defaultButton() :
    #     funcYes()
    # else:
    #     funcNo
def SetWidthToScreen(size):
    screenSize = QDesktopWidget().screenGeometry(-1)
    curRateWidth = screenSize.width() / 1920
    return int(size*curRateWidth)

def SetHeightToScreen(size):
    screenSize = QDesktopWidget().screenGeometry(-1)
    curRateHeight = screenSize.height() / 1080
    return int(size*curRateHeight)
def SetRateToScreen(size):
    screenSize = QDesktopWidget().screenGeometry(-1)
    curRateWidth = screenSize.width() / 1920
    curRateHeight = screenSize.height() / 1080
    currentRate = math.sqrt(curRateHeight*curRateWidth)
    return int(size*currentRate)