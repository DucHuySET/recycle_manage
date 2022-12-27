from datetime import datetime

class ImportData:
    def __init__(self) -> None:
        self.id = 0
        self.measStaff = ''
        self.collStaff = ''
        self.pack = ''
        self.scrapType = ''
        self.weight = 0
        self.time = datetime.now()