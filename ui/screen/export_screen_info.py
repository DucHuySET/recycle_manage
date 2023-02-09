# This Python file uses the following encoding: utf-8
import time
import serial
import sqlite3
from model.export_info_model import ExportInfoData
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from ui.base_widget.utils_widget import *
from send_read_rs232 import *
from core.values.strings import AppStr
from ui.base_widget.utlis_func import *

class ExportScreenInfo (QMainWindow):
    def __init__(self, stackWidget, mainWindow, exportScreen):
        self.stackWidget = stackWidget
        self.mainWindow = mainWindow
        self.exportScreen = exportScreen
        super().__init__()
        self.setWindowTitle("Waste Management")
        # self.setGeometry(0,0,1000,1000)
        self.setStyleSheet("background-color: #1d212d")
        self.uiComponents()
        self.show()
        self.currentTurn = 0
        self.generalConnect = sqlite3.connect('database\general.db')
        self.generalCursor = self.generalConnect.cursor()
        self.exportInfoData = ExportInfoData()
        self.checkPakage = False
        self.checkType = False
        self.checkScale= False #TODO: checkScale
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)
        self.column01.setAlignment(Qt.AlignTop)

        self.turn_info = QLabel('Thông tin lượt cân đầu ra')
        self.turn_info.setFont(QFont("Arial", SetRateToScreen(20)))
        self.turn_info.setStyleSheet("color: white")
        self.column01.addWidget(self.turn_info)

        self.divider01 = buildDivider()
        self.column01.addWidget(self.divider01)

        self.body = QHBoxLayout()
        # body.setStretch(1, 50)
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

        self.column_Input = QVBoxLayout()
        self.column_Input.setAlignment(Qt.AlignTop)
        self.column_Input.setSpacing(50)
        self.input_Field.setLayout(self.column_Input)
        
        self.declare = QLabel('Quy trình cân phế liệu xuất bán')
        self.declare.setObjectName('declare')
        self.declare.setFixedHeight(SetHeightToScreen(80))
        self.declare.setStyleSheet(f'''
        QLabel#declare {{
            background-color: transparent;
            border: none;
            border-radius: 0px;
            color: white;
        }}''')
        self.declare.setFont(QFont("Arial", SetRateToScreen(20)))
        self.column_Input.addWidget(self.declare)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem('Lượt cân'))
        self.input1 = buildInputForm(500, 80)
        self.input1.input.setText("1")
        self.input1.input.clearFocus()
        self.input1.focusNextPrevChild(True)
        self.input1.input.textChanged.connect(self.setTurn)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.addWidget(buildCardItem('Thùng bì'))
        self.input2 = buildInputForm(500, 80)
        self.input2.input.textChanged.connect(self.setPackage)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        
        self.row3 = QHBoxLayout()
        self.row3.addWidget(buildCardItem('Chủng loại phế liệu'))
        self.input3 = buildInputForm(500, 80)
        self.input3.input.textChanged.connect(self.setType)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)

        self.row4 = QHBoxLayout()
        self.row4.addWidget(buildCardItem('Xác nhận thông tin cân'))
        self.input4 = buildInputForm(500, 80)
        self.input4.input.textChanged.connect(self.setTurnInfo)
        self.input4.input.setMaxLength(20)
        self.row4.addWidget(self.input4)
        self.column_Input.addLayout(self.row4)

        self.rowConfirm = QHBoxLayout()
        self.rowConfirm.setAlignment(Qt.AlignHCenter)
        self.column_Input.addLayout(self.rowConfirm)
        self.confirmButton = buildButton("Xác nhận thông tin", 500, 60)
        self.confirmButton.clicked.connect(self.readScaleData)
        self.rowConfirm.addWidget(self.confirmButton)

        self.column_record = QVBoxLayout()
        self.column_record.setAlignment(Qt.AlignTop)
        self.recordField.setLayout(self.column_record)

        self.recordLabel = QLabel('Thông tin bản ghi')
        self.recordLabel.setFixedHeight(SetHeightToScreen(100))
        self.recordLabel.setStyleSheet(f'''
        QLabel {{
            background-color: transparent;
            border: none;
            border-radius: 0px;
            color: white;
        }}''')
        self.recordLabel.setFont(QFont("Arial", SetRateToScreen(20)))
        self.column_record.addWidget(self.recordLabel)

        self.turn = buildLabel('Lượt cân: ')
        self.turn.setText('Lượt cân: 1')
        self.column_record.addWidget(self.turn)

        self.package = buildLabel('Thùng bì: ')
        self.column_record.addWidget(self.package)

        self.type = buildLabel('Chủng loại phế liệu: ')
        self.column_record.addWidget(self.type)

        self.measInfo = buildLabel('Thông tin cân: ')
        self.column_record.addWidget(self.measInfo)

        self.rowAction = QHBoxLayout()
        self.rowAction.setSpacing(150)
        self.column_record.addLayout(self.rowAction)

        self.saveButton = buildButton("Lưu", 300, 80)
        self.saveButton.clicked.connect(self.tryTurnSave)
        self.rowAction.addWidget(self.saveButton)

        self.cancelButton = buildButton("Hủy", 300, 80)
        self.cancelButton.clicked.connect(self.turnCancel)
        self.rowAction.addWidget(self.cancelButton)

        self.column_record.addWidget(sizedBox10())

        self.back_button = buildButton("Quay lại màn hình khai báo", 750, 80)
        self.back_button.clicked.connect(self.goToExportScr)
        self.column_record.addWidget(self.back_button)

        self.main_button = buildButton("Quay lại màn hình chính", 750, 80)
        self.main_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.main_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def getPackInfo(self, inputId):
        selectPackWithId = """
            SELECT * FROM pack WHERE id == {id}
        """.format(id = inputId)
        self.generalCursor.execute(selectPackWithId)
        result = self.generalCursor.fetchone()
        print(result[0])
        return result
    def getTypeInfo(self, inputId):
        selectTypeWithId = """
            SELECT * FROM scrap WHERE id == {id}
        """.format(id = inputId)
        self.generalCursor.execute(selectTypeWithId)
        result = self.generalCursor.fetchone()
        print(result[0])
        return result
    def goToExportScr(self):
        self.exportScreen.input1.input.setFocus()
        self.stackWidget.setCurrentWidget(self.exportScreen)
    def goToMainScr(self):
        self.exportScreen.clearField()
        self.exportScreen.input1.input.setFocus()
        self.exportScreen.carPixmap = QPixmap('assets\\images\\1280x720-grey-solid-color.jpg')
        self.exportScreen.carPicture.setPixmap(self.exportScreen.carPixmap)
        self.stackWidget.setCurrentWidget(self.mainWindow)
    def setTurn(self):
        self.turn.setText('Lượt cân: ' + self.input1.input.text())
    def setPackage(self):
        packId = -1
        try: 
            packId = int(self.input2.input.text())
            packInfo = self.getPackInfo(packId)
            self.package.setText('Thùng bì: ' + packInfo[1])
            self.exportInfoData.pack = packInfo[1]
            self.checkPakage = True
        except Exception:
            packId = -1
            self.package.setText('Không tìm thấy thùng bì')
            self.checkPakage = False
    def setType(self):
        typeId = -1
        try: 
            typeId =  int(self.input3.input.text())
            # self.importData.scrapType = typeId
            typeInfo = self.getTypeInfo(typeId)
            self.type.setText('Chủng loại phế liệu: ' + typeInfo[1])
            self.exportInfoData.scrap = typeInfo[1]
            self.checkType = True
        except Exception:
            typeId = -1
            self.type.setText('Không tìm thấy loại phế liệu')
            self.checkType = False
    def setTurnInfo(self):
        self.measInfo.setText('Thông tin lượt cân: ' + self.input4.input.text())
    def tryTurnSave(self):
        if self.checkPakage and self.checkType :
            self.saveTurn()
        else:
            if not self.checkPakage:
                self.input2.input.setFocus()
            elif not self.checkType:
                self.input3.input.setFocus()
            ShowNotification(AppStr.ERROR_SAVE_INFO, AppStr.ERROR_FIELD_CONTENTS, self.saveTurn)
    def turnCancel(self):
        self.currentTurn = int(self.input1.input.text())
        self.clearField()
        self.input1.input.setText(str(self.currentTurn))
        self.input2.input.setFocus()
        print("canceled")
    def clearField(self):
        self.input1.input.clear()
        self.input2.input.clear()
        self.input3.input.clear()
        self.input4.input.clear()
    def readScaleData(self):
        try:
            ser = serial.Serial(
                port='COM8',
                baudrate=9600,
                timeout=1,
                parity=serial.PARITY_ODD,
                stopbits=serial.STOPBITS_TWO,
                bytesize=serial.EIGHTBITS
            )

            ser.isOpen()

            for i in range(10):
                bytesToRead = ser.inWaiting()
                data = ser.read(bytesToRead)
                time.sleep(2)
                # print(data)
                self.dataStr = str(data).replace("b\'", "").replace("\'","")
                print(self.dataStr)
                if self.dataStr != "":
                    self.input4.input.setText(self.dataStr)
                    break
            # self.scaleData = readRs232()
            # if self.dataStr != "":
            #     self.input4.input.setText(self.scaleData)
        except Exception:
            print(AppStr.CANT_READ_SCALE)
    def saveTurn(self):
        self.generalCursor.execute(
            """
                SELECT id FROM export_info
            """
        )
        tableLength = len(self.generalCursor.fetchall())
        self.exportInfoData.id = tableLength + 1
        self.exportInfoData.exportId = self.mainWindow.exportId
        self.currentTurn = int(self.input1.input.text())
        self.exportInfoData.turn = int(self.currentTurn)
        try:
            self.exportInfoData.weight = float(self.input4.input.text())
        except :
            self.exportInfoData.weight = -1
        self.generalCursor.execute(
            """
                INSERT INTO export_info VALUES (
                    ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                self.exportInfoData.id, 
                self.exportInfoData.exportId,
                self.exportInfoData.turn,
                self.exportInfoData.pack,
                self.exportInfoData.scrap,
                self.exportInfoData.weight,
                self.exportInfoData.time
                )
        )
        self.generalConnect.commit()

        self.currentTurn = int(self.input1.input.text())
        self.clearField()
        self.input1.input.setText(str(self.currentTurn+1))
        self.input2.input.setFocus()
        print("saved")