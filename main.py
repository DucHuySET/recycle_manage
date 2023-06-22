# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

from lib.app_ui.screen.main_screen import MainWindow




def main():
    # def exitHandler():
        # import_screen.generalConnect.close()
        # export_screen.generalConnect.close()

    # def goToImportScr():
    #     import_screen = Import_screen(widget_stack, mainWindow)
    #     widget_stack.addWidget(import_screen)
    #     widget_stack.setCurrentWidget(import_screen)
    #     print(widget_stack.count())
    #     import_screen.input1.input.setFocus()

    # export_screen = None

    # def goToExportScr():
    #     # global export_screen
    #     export_screen = ExportScreen(widget_stack, mainWindow)
    #     widget_stack.addWidget(export_screen)
    #     export_screen.next_button.clicked.connect(goToInfoScr)
    #     widget_stack.setCurrentWidget(export_screen)
    #     print(widget_stack.count())
    #     # return export_screen

    # def goToInfoScr():
    #     export_screen = goToExportScr()
    #     export_screen_info = ExportScreenInfo(widget_stack, mainWindow, export_screen)
    #     widget_stack.addWidget(export_screen_info)
    #     if export_screen.canGo:
    #         widget_stack.setCurrentWidget(export_screen_info)
    #         mainWindow.exportId = widget_stack.export_screen.exportData.id
    #         export_screen_info.input2.input.setFocus()

    app = QApplication(sys.argv)
    # app.aboutToQuit.connect(exitHandler)

    appWindow = QMainWindow()
    appWindow.setWindowTitle('Quản lý nhập - xuất phế liệu')

    widget_stack = QStackedWidget(appWindow)
    appWindow.setCentralWidget(widget_stack)

    mainWindow = MainWindow()
    # mainWindow.button_import.clicked.connect(goToImportScr)
    # mainWindow.button_export.clicked.connect(goToExportScr)
    # widget_stack.export_screen.next_button.clicked.connect(goToInfoScr)

    # import_screen = Import_screen(widget_stack, mainWindow)
    # export_screen = ExportScreen(widget_stack, mainWindow)
    # export_screen_info = ExportScreenInfo(widget_stack, mainWindow, export_screen)

    
    # mainWindow.button_import.clicked.connect(goToImportScr)

    
    # mainWindow.button_export.clicked.connect(goToExportScr)


    
    # export_screen.next_button.clicked.connect(goToInfoScr)

    

    widget_stack.addWidget(mainWindow)
    # widget_stack.addWidget(import_screen)
    # widget_stack.addWidget(export_screen)
    # widget_stack.addWidget(export_screen_info)

    
    appWindow.showMaximized()
    # start the app
    sys.exit(app.exec_())

    
if __name__ == "__main__":
    main()