# This Python file uses the following encoding: utf-8
import time
import serial
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui.base_widget.utils_widget import *
from model.importModel import *

class Import_screen(QMainWindow):
    def __init__(self, stackWidget, mainWindow):
        self.stackWidget = stackWidget
        self.mainWindow = mainWindow
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: #1d212d")
        self.uiComponents()
        self.show()
        # self.importConnect = sqlite3.connect('database\import.db')
        # self.importCursor = self.importConnect.cursor()
        self.generalConnect = sqlite3.connect('database\general.db')
        self.generalCursor = self.generalConnect.cursor()
        self.importData = ImportData()
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)

        self.turn_info = QLabel('Thông tin lượt cân đầu vào')
        self.turn_info.setFont(QFont("Arial", 20))
        self.turn_info.setStyleSheet("color: white")
        self.column01.addWidget(self.turn_info)

        # self.divider01 = QLabel('')
        # self.divider01.setObjectName('divider01')
        # self.divider01.setFixedHeight(2)
        # self.divider01.setStyleSheet(f'''
        # QLabel#divider01 {{
        #     background-color: white;
        #     border-radius: 20px;
        #     border: 2px solid black;
        # }}''')
        # self.column01.addWidget(self.divider01)

        self.body = QHBoxLayout()
        self.column01.addLayout(self.body)

        self.input_Field = QWidget()
        self.input_Field.setObjectName("input_Field")
        self.input_Field.setFixedSize(1100,900)
        self.input_Field.setStyleSheet(f'''
        QWidget#input_Field {{
            background-color: #2e2e2e;
            border: none;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.input_Field)

        self.recordField = QWidget()
        self.recordField.setObjectName("recordField")
        self.recordField.setStyleSheet(f'''
        QWidget#recordField {{
            background-color: #2e2e2e;
            border: none;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.recordField)

        self.column_Input = QVBoxLayout()
        self.column_Input.setAlignment(Qt.AlignTop)
        self.column_Input.setSpacing(50)
        self.input_Field.setLayout(self.column_Input)
        
        self.declare = QLabel('Quy trình nhập phế liệu đầu vào')
        self.declare.setObjectName('declare')
        self.declare.setFixedHeight(80)
        self.declare.setContentsMargins(12,0,12,0)
        self.declare.setStyleSheet(f'''
        QLabel#declare {{
            background-color: transparent;
            border: none;
            border-radius: 0px;
            color: white;
        }}''')
        self.declare.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.declare)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem(700, 80, 'Nhân viên phụ trách cân đầu vào'))
        self.input1 = buildInputForm(400, 80)
        self.input1.input.textChanged.connect(self.setStaffNameMeas)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setContentsMargins(0,0,0,0)
        self.row2.addWidget(buildCardItem(700, 80, 'Nhân viên tập kết phế liệu'))
        self.input2 = buildInputForm(400, 80)
        self.input2.input.textChanged.connect(self.setStaffNameColl)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        
        self.row3 = QHBoxLayout()
        self.row3.setContentsMargins(0,0,0,0)
        self.row3.addWidget(buildCardItem(700, 80, 'Thùng bì'))
        self.input3 = buildInputForm(400, 80)
        self.input3.input.textChanged.connect(self.setPackage)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)

        self.row4 = QHBoxLayout()
        self.row4.setContentsMargins(0,0,0,0)
        self.row4.addWidget(buildCardItem(700, 80, 'Chủng loại phế liệu'))
        self.input4 = buildInputForm(400, 80)
        self.input4.input.textChanged.connect(self.setType)
        self.row4.addWidget(self.input4)
        self.column_Input.addLayout(self.row4)

        self.row5 = QHBoxLayout()
        self.row5.setContentsMargins(0,0,0,0)
        self.row5.addWidget(buildCardItem(700, 80, 'Xác nhận khối lượng cân'))
        self.input5 = buildInputForm(400, 80)
        self.input5.input.textChanged.connect(self.setInfo)
        self.row5.addWidget(self.input5)
        self.column_Input.addLayout(self.row5)

        self.rowConfirm = QHBoxLayout()
        self.rowConfirm.setAlignment(Qt.AlignHCenter)
        self.column_Input.addLayout(self.rowConfirm)
        self.confirmButton = buildButton("Xác nhận thông tin cân", 500, 60)
        self.confirmButton.clicked.connect(self.readScaleData)
        self.rowConfirm.addWidget(self.confirmButton)

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
        self.recordLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.recordLabel)

        self.staffNameMeas = QLabel('Tên nhân viên cân: ')
        self.staffNameMeas.setFixedHeight(100)
        self.staffNameMeas.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.staffNameMeas.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.staffNameMeas)

        self.staffNameColl = QLabel('Nhân viên tập kết phế liệu: ')
        self.staffNameColl.setFixedHeight(100)
        self.staffNameColl.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.staffNameColl.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.staffNameColl)

        self.package = QLabel('Thùng bì: ')
        self.package.setFixedHeight(100)
        self.package.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.package.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.package)

        self.type = QLabel('Chủng loại phế liệu: ')
        self.type.setFixedHeight(100)
        self.type.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.type.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.type)

        self.measInfo = QLabel('Thông tin cân: ')
        self.measInfo.setFixedHeight(100)
        self.measInfo.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.measInfo.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.measInfo)

        self.saveButton = buildButton("Lưu", 750, 80)
        # self.saveButton.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.saveButton)
        self.saveButton.clicked.connect(self.saveInfo)

        self.back_button = buildButton("Quay lại", 750, 80)
        self.back_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.back_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

    def getStaffInfo(self, inputId):
        selectStaffWithId = """
            SELECT * FROM staff WHERE id == {id}
        """.format(id = inputId)
        self.generalCursor.execute(selectStaffWithId)
        result = self.generalCursor.fetchone()
        print(result[0])
        return result
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

        # self.setStaffName()
    def goToMainScr(self):
        # self.generalConnect.close()
        self.stackWidget.setCurrentWidget(self.mainWindow)
    def setStaffNameMeas(self):
        staffId = -1
        try: 
            staffId =  int(self.input1.input.text())
            
            staffInfo = self.getStaffInfo(staffId)
            self.staffNameMeas.setText('Tên nhân viên cân: ' + staffInfo[1])
            self.importData.measStaff = staffInfo[1]
        except Exception:
            staffId = -1
            self.staffNameMeas.setText('Không tìm thấy nhân viên')
            
    def setStaffNameColl(self):
        staffId = -1
        try: 
            staffId =  int(self.input2.input.text())
            
            staffInfo = self.getStaffInfo(staffId)
            self.staffNameColl.setText('Nhân viên cân tập kết: ' + staffInfo[1])
            self.importData.collStaff = staffInfo[1]
        except Exception:
            staffId = -1
            self.staffNameColl.setText('Không tìm thấy nhân viên')
    def setPackage(self):
        packId = -1
        try: 
            packId =  int(self.input3.input.text())
            packInfo = self.getPackInfo(packId)
            self.package.setText('Thùng bì: ' + packInfo[1])
            self.importData.pack = packInfo[1]
        except Exception:
            packId = -1
            self.package.setText('Không tìm thấy thùng bì')
    def setType(self):
        typeId = -1
        try: 
            typeId =  int(self.input4.input.text())
            # self.importData.scrapType = typeId
            typeInfo = self.getTypeInfo(typeId)
            self.type.setText('Chủng loại phế liệu: ' + typeInfo[1])
            self.importData.scrapType = typeInfo[1]
        except Exception:
            typeId = -1
            self.type.setText('Không tìm thấy loại phế liệu')
    def setInfo(self):
        try:
            self.importData.weight = float(self.input5.input.text())
        except Exception:
            self.measInfo.setText('Khối lượng cân: ' + '0.0')
        self.measInfo.setText('Khối lượng cân: ' + self.input5.input.text())
    def saveInfo(self):
        self.generalCursor.execute(
            """
                SELECT id FROM import
            """
        )
        tableLength = len(self.generalCursor.fetchall())
        self.importData.id = tableLength + 1
        self.generalCursor.execute(
            """
                INSERT INTO import VALUES (
                    ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                self.importData.id, 
                self.importData.measStaff,
                self.importData.collStaff,
                self.importData.pack,
                self.importData.scrapType,
                self.importData.weight,
                self.importData.time
                )
        )
        self.generalConnect.commit()
        # self.generalConnect.close()
        self.resetInfo()
        self.stackWidget.setCurrentWidget(self.mainWindow)
    def resetInfo(self):
        self.input1.input.clear()
        self.input2.input.clear()
        self.input3.input.clear()
        self.input4.input.clear()
        self.input5.input.clear()
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
                    self.input5.input.setText(self.dataStr)
                    break
            # self.scaleData = readRs232()
            # if self.dataStr != "":
            #     self.input4.input.setText(self.scaleData)
        except Exception:
            print('Không đọc được giá trị cân')