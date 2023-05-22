# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

from app_ui.screen.import_screen import *
from app_ui.screen.export_screen import *
from app_ui.screen.export_screen_info import *
from app_ui.screen.main_screen import *
from app_ui.base_widget.utils_widget import *
from app_ui.base_widget.utlis_func import *




def main():
    def exitHandler():
        pass
        # import_screen.generalConnect.close()
        # export_screen.

    def goToImportScr():
        import_screen = Import_screen(widget_stack, mainWindow)
        widget_stack.addWidget(import_screen)
        widget_stack.setCurrentWidget(import_screen)
        print(widget_stack.count())
        import_screen.input1.input.setFocus()

    # export_screen = None

    def goToExportScr():
        # global export_screen
        export_screen = ExportScreen(widget_stack, mainWindow)
        widget_stack.addWidget(export_screen)
        export_screen.next_button.clicked.connect(goToInfoScr)
        widget_stack.setCurrentWidget(export_screen)
        print(widget_stack.count())
        # return export_screen

    def goToInfoScr():
        export_screen = goToExportScr()
        export_screen_info = ExportScreenInfo(widget_stack, mainWindow, export_screen)
        widget_stack.addWidget(export_screen_info)
        if export_screen.canGo:
            widget_stack.setCurrentWidget(export_screen_info)
            mainWindow.exportId = widget_stack.export_screen.exportData.id
            export_screen_info.input2.input.setFocus()

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(exitHandler)

    widget_stack = QStackedWidget()
    widget_stack.setFixedSize(SetWidthToScreen(1920), SetHeightToScreen(1080))
    widget_stack.setWindowTitle('Quản lý nhập - xuất phế liệu')
    widget_stack.setWindowIcon(QIcon('D:/Qt/Project/Test_Qt_Creator/assets/images/CTARG.png'))
    app.setStyleSheet('QApplication{background-color: yellow; color: blue}')

    mainWindow = MainWindow()
    mainWindow.button_import.clicked.connect(goToImportScr)
    mainWindow.button_export.clicked.connect(goToExportScr)
    # widget_stack.export_screen.next_button.clicked.connect(goToInfoScr)

    # import_screen = Import_screen(widget_stack, mainWindow)
    # export_screen = ExportScreen(widget_stack, mainWindow)
    # export_screen_info = ExportScreenInfo(widget_stack, mainWindow, export_screen)

    
    # mainWindow.button_import.clicked.connect(goToImportScr)

    
    # mainWindow.button_export.clicked.connect(goToExportScr)


    
    # export_screen.next_button.clicked.connect(goToInfoScr)

    

    widget_stack.addWidget(mainWindow)
    print(widget_stack.count())
    # widget_stack.addWidget(import_screen)
    # widget_stack.addWidget(export_screen)
    # widget_stack.addWidget(export_screen_info)

    #widget_stack.showMaximized()
    #widget_stack.showFullScreen()
    widget_stack.show()
    # start the app
    sys.exit(app.exec_())

    
if __name__ == "__main__":
    main()