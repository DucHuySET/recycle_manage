# This Python file uses the following encoding: utf-8
import sqlite3
import cv2
from datetime import datetime
# from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from app_ui.base_widget.utils_widget import *
from model.expotModel import *
from core.values.strings import AppStr
from Detect_license_plate.deploy import *
from app_ui.base_widget.utlis_func import *

class ExportScreen (QMainWindow):
    def __init__(self, stackWidget, mainWindow):
        self.stackWidget = stackWidget
        self.mainWindow = mainWindow
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setStyleSheet("background-color: #1d212d")
        self.uiComponents()
        self.show()
        self.generalConnect = sqlite3.connect('database\general.db')
        self.generalCursor = self.generalConnect.cursor()
        self.exportData = ExportData()
        self.imageLink = ''
        self.checkStaffMeas= False
        self.checkComp = False
        self.checkCar= False #TODO: checkCar valid
        self.canGo = False
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)
        self.column01.setAlignment(Qt.AlignTop)

        self.turn_info = QLabel('Thông tin lượt cân đầu ra')
        self.turn_info.setFont(QFont("Arial", SetRateToScreen(20)))
        self.turn_info.setStyleSheet("color: white")
        self.column01.addWidget(self.turn_info)

        # self.divider01 = buildDivider()
        # self.column01.addWidget(self.divider01)

        self.body = QHBoxLayout()
        self.column01.addLayout(self.body)

        self.input_Field = QWidget()
        self.input_Field.setObjectName("input_Field")
        self.input_Field.setFixedSize(SetWidthToScreen(1100),SetHeightToScreen(900))
        self.input_Field.setStyleSheet(f'''
        QWidget {{
            background-color: #2e2e2e;
            border: none;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.input_Field)

        self.recordField = QWidget()
        self.recordField.setObjectName("recordField")
        self.recordField.setStyleSheet(f'''
        QWidget {{
            background-color: #2e2e2e;
            border: none;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.recordField)


        # inputField = buildCardBase(500,900)
        # body.addWidget(inputField)

        # recordField = buildCardBase(750,900)
        # body.addWidget(recordField)

        self.column_Input = QVBoxLayout()
        self.column_Input.setAlignment(Qt.AlignTop)
        self.column_Input.setSpacing(SetHeightToScreen(50))
        self.input_Field.setLayout(self.column_Input)
        
        self.declare = QLabel('Quy trình khai báo thu gom phế liệu')
        self.declare.setObjectName('declare')
        self.declare.setFixedHeight(SetHeightToScreen(80))
        self.declare.setStyleSheet(
            "background-color: transparent;"
            "border: none;"
            "border-radius: 0px;"
            "color: white;"
        )
        self.declare.setFont(QFont("Arial", SetRateToScreen(20)))
        self.column_Input.addWidget(self.declare)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem('Nhân viên phụ trách cân đầu vào'))
        self.input1 = buildInputForm(500, 80)
        self.input1.input.textChanged.connect(self.setStaffName)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setContentsMargins(0,0,0,0)
        self.row2.addWidget(buildCardItem('Công ty thu gom phế liệu'))
        self.input2 = buildInputForm(500, 80)
        self.input2.input.textChanged.connect(self.setCompName)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        self.input2.input.returnPressed.connect(self.detectLicense)
        
        self.row3 = QHBoxLayout()
        self.row3.setContentsMargins(0,0,0,0)
        self.row3.addWidget(buildCardItem('Xe vận tải'))
        self.input3 = buildInputForm(500, 80, False)
        self.input3.input.textChanged.connect(self.setCarLabel)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)
        

        # self.rowConfirm = QHBoxLayout()
        # self.rowConfirm.setAlignment(Qt.AlignHCenter)
        # self.column_Input.addLayout(self.rowConfirm)
        # self.confirmButton = buildButton("Xác nhận xe", SetWidthToScreen(500), SetHeightToScreen(60))
        # # self.confirmButton.clicked.connect(self.getLicensePlate)
        # self.rowConfirm.addWidget(self.confirmButton)

        self.carPicture = QLabel()
        self.carPixmap = QPixmap('assets\\images\\1280x720-grey-solid-color.jpg')
        self.carPicture.setPixmap(self.carPixmap)
        self.carPicture.setFixedSize(min(600, self.carPixmap.width()), min(350, self.carPixmap.height()))
        self.rowPicture = QHBoxLayout()
        self.rowPicture.setAlignment(Qt.AlignHCenter)
        self.rowPicture.addWidget(self.carPicture)
        self.column_Input.addLayout(self.rowPicture)

        self.column_record = QVBoxLayout()
        self.column_record.setAlignment(Qt.AlignTop)
        self.recordField.setLayout(self.column_record)

        self.recordLabel = QLabel('Thông tin bản ghi')
        self.recordLabel.setFixedHeight(100)
        self.recordLabel.setStyleSheet(f'''
        QLabel {{
            background-color: transparent;
            border: none;
            border-radius: 0px;
            color: white;
        }}''')
        self.recordLabel.setFont(QFont("Arial", SetRateToScreen(20)))
        self.column_record.addWidget(self.recordLabel)

        self.staffName = buildLabel('Tên nhân viên: ')
        self.column_record.addWidget(self.staffName)

        self.compName = buildLabel('Tên công ty: ')
        self.column_record.addWidget(self.compName)

        self.carLabel = buildLabel('Biển kiểm soát: ')
        self.column_record.addWidget(self.carLabel)

        self.back_button = buildButton("Quay lại", 750,80)
        self.back_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.back_button)

        self.next_button = buildButton("Thông tin lượt cân", 750, 80)
        # self.next_button.clicked.connect(self.goToInfoScr)
        self.next_button.clicked.connect(self.trySaveAndGo)
        self.column_record.addWidget(self.next_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def getStaffInfo(self, inputId):
        selectStaffWithId = """
            SELECT * FROM staff WHERE id == {id}
        """.format(id = inputId)
        self.generalCursor.execute(selectStaffWithId)
        result = self.generalCursor.fetchone()
        print(result[0])
        return result
    def getCompInfo(self, inputId):
        selectCompWithId = """
            SELECT * FROM company WHERE id == {id}
        """.format(id = inputId)
        self.generalCursor.execute(selectCompWithId)
        result = self.generalCursor.fetchone()
        print(result[0])
        return result
    def goToMainScr(self):
        self.carPixmap = QPixmap('assets\\images\\1280x720-grey-solid-color.jpg')
        self.carPicture.setPixmap(self.carPixmap)
        self.stackWidget.setCurrentWidget(self.mainWindow)
    # def goToInfoScr(self):
    #     self.stackWidget.setCurrentWidget(self.exportScreenInfo)
    def setStaffName(self):
        staffId = -1
        try: 
            staffId = int(self.input1.input.text())
            staffInfo = self.getStaffInfo(staffId)
            self.staffName.setText('Thông tin nhân viên: ' + staffInfo[1])
            self.exportData.measStaff = staffInfo[1]
            self.checkStaffMeas = True
        except Exception:
            staffId = -1
            self.exportData.measStaff = 'Staff Not Found'
            self.staffName.setText('Không tìm thấy nhân viên')
            self.checkStaffMeas = False
    def setCompName(self):
        compId = -1
        try:
            compId = int(self.input2.input.text())
            compInfo = self.getCompInfo(compId)
            self.compName.setText('Tên công ty: ' + compInfo[1])
            self.exportData.compName = compInfo[1]
            self.checkComp = True
        except Exception:
            compId = -1
            self.exportData.compName = 'Company Not Found'
            self.compName.setText('Không tìm thấy công ty')
            self.checkComp  = False
    def setCarLabel(self):
        self.carLabel.setText('Biển kiểm soát: ' + self.input3.input.text())
    # def getLicensePlate(self):
    #     self.takePhoto()
    #     self.detectLicense()
    #     print('bks')
    def takePhoto(self):
        capture = cv2.VideoCapture()
        image = capture.read()
        dateTime = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
        if image:
            cv2.imshow(dateTime, image)
            self.imageLink = "database\\truck_image\\" + dateTime + ".png"
            cv2.imwrite(self.imageLink, image)
            cv2.waitKey(0)
            cv2.destroyWindow(dateTime)
        else:
            print(AppStr.NO_IMAGE_DETECT)
    def detectLicense(self):
        try:
            self.input3.input.setText(AppStr.PLEASE_WAIT)
            print(AppStr.PLEASE_WAIT)
            # self.exportData.truck = deploy("Detect_license_plate\\test_images\\5.jpg")
            # self.exportData.truck = deploy(self.imageLink)
            # self.exportData.truck = str(self.exportData.truck).replace(';', '')
            self.exportData.truck = str(deploy("Detect_license_plate\\test_images\\5.jpg")).replace(';', '')
            self.exportData.evident = self.imageLink
            self.input3.input.setText(self.exportData.truck)
            # self.carPixmap = QPixmap(self.imageLink)
            self.carPixmap = QPixmap("Detect_license_plate\\test_images\\5.jpg")
            self.carPicture.setPixmap(self.carPixmap)
            print(AppStr.DETECT_SUCCESS)
        except Exception:
            print(AppStr.DETECT_FAILED)
    def trySaveAndGo(self):
        if self.checkStaffMeas and self.checkComp:
            self.saveInfo()
        else:
            self.canGo = False
            if not self.checkStaffMeas:
                self.input1.input.setFocus()
            elif not self.checkComp:
                self.input2.input.setFocus()
            ShowNotification(AppStr.ERROR_SAVE_INFO, AppStr.ERROR_FIELD_CONTENTS, self.saveInfo)
    def clearField(self):
        self.input1.input.clear()
        self.input2.input.clear()
        self.input3.input.clear()
    def saveInfo(self):
        self.generalCursor.execute(
        """
            SELECT id FROM export
        """
        )
        tableLength = len(self.generalCursor.fetchall())
        self.exportData.id = tableLength + 1
        self.generalCursor.execute(
            """
                INSERT INTO export VALUES (
                    ?, ?, ?, ?, ?
                )
            """, (
                self.exportData.id, 
                self.exportData.measStaff,
                self.exportData.compName,
                self.exportData.truck,
                self.exportData.time
                )
        )
        self.generalConnect.commit()
        self.canGo = True
