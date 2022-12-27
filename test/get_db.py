import sqlite3

class Staff:
    def __init__(self, list):
        if (len(list) == 7):
            self.id = list[0]
            self.name = list[1]
            self.unit = list[2]
            self.function = list[3]
            self.contact = list[4]
            self.createTime = list[5]
            self.editTime = list[6]

listStaff = []

connection = sqlite3.connect('database\general.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM staff")

rows = cursor.fetchall()

for row in rows:
    staffTmp = Staff(row)
    listStaff.append(staffTmp)

for staff in listStaff:
    print(staff.contact)

connection.close()