import sqlite3

from staff_db import *

class StaffRepository:
    def __init__ (self):
        self.staffConnect = sqlite3.connect('database\general.db')
        self.staffCursor = self.staffConnect.cursor()
    def close(self):
        self.staffConnect.close()
    def creatTable(self):
        create_table_staff = """
            CREATE TABLE staff IF NOT EXIST (
                id integer,
                name text,
                unit text,
                function integer,
                contact text,
                createTime text,
                editTime text
            )
        """
        self.staffCursor.execute(create_table_staff)
        self.staffConnect.commit()
    def insertTable(self, staffDb: StaffDB):
        insert_to_staff = """
            INSERT INTO staff VALUES (
                {},{},{},{},{},{},{}
            )
        """.format(staffDb.id, staffDb.name, staffDb.unit, staffDb.function, staffDb.contact, staffDb.createTime, staffDb.editTime)
        self.staffCursor.execute(insert_to_staff)
    def getStaffDbList(self):
        listStaff = []
        rows = self.staffCursor.execute("SELECT * FROM staff").fetchall()
        for row in rows:
            staffTmp = StaffDB(row)
            listStaff.append(staffTmp)
        return listStaff

# staffRepository = StaffRepository()
# checkEmpty = staffRepository.staffCursor.fetchone()

# if checkEmpty is None:
#     staffRepository.creatTable()
# else:
#     staffRepository