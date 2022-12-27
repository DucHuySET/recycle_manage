class StaffDB:
    def __init__(self, list):
        if (len(list) == 7):
            self.id = list[0]
            self.name = list[1]
            self.unit = list[2]
            self.function = list[3]
            self.contact = list[4]
            self.createTime = list[5]
            self.editTime = list[6]