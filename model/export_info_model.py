from datetime import datetime

class ExportInfoData:
    def __init__(self):
        self.id = 0
        self.exportId = 0
        self.turn = 0
        self.pack = ''
        self.scrap = ''
        self.weight = 0.0
        self.time = datetime.now()