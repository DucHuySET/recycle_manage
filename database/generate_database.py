import sqlite3

connection = sqlite3.connect('database\general.db')

cursor = connection.cursor()

### create table for staff
### function, 0: nhân viên cân, 1: nhân viên tập kết phế liệu
create_table_staff = """
    CREATE TABLE staff (
        id integer,
        name text,
        unit text,
        function integer,
        contact text,
        createTime text,
        editTime text
    )
"""

### create table for company and link to truck table
create_table_company = """
    CREATE TABLE company (
        id integer,
        name text,
        contact integer,
        taxCode text,
        address text,
        contractCode text,
        createTime text,
        editTime text
    )
"""

### create table for trucks
create_table_truck = """
    CREATE TABLE truck (
        id integer,
        comId integer,
        plateCode text,
        truckType text,
        capacity text,
        driverName text,
        driverContact integer,
        driverId integer,
        createTime text,
        editTime text
    )
"""

### create table for types of scrap
create_table_scrap = """
    CREATE TABLE scrap (
        id integer,
        name text,
        info text,
        unit text,
        createTime text,
        editTime text
    )
"""

### create table for packs
create_table_pack = """
    CREATE TABLE pack (
        id integer,
        name text,
        weight real,
        special bool,
        createTime text,
        editTime text
    )
"""

### create table for import
create_table_import = """
    CREATE TABLE import (
        id integer,
        mea_staff text,
        coll_staff text,
        pack text,
        type text,
        weight real,
        time text
    )
"""

# ### create table for import
# create_table_import = """
#     CREATE TABLE import (
#         id integer,
#         mea_staffid integer,
#         mea_staff text,
#         coll_staff_id integer,
#         coll_staff text,
#         pack_id integer,
#         pack text,
#         type_id integer,
#         type text,
#         weight real,
#         time text
#     )
# """

### create table for export
create_table_export = """
    CREATE TABLE export (
        id integer,
        measstaff text,
        comp_name text,
        truck text,
        time text
    )
"""

# ### create table for export
# create_table_export = """
#     CREATE TABLE export (
#         id integer,
#         mea_staff_id integer,
#         measstaff text,
#         coomp_id integer,
#         comp_name text,
#         truck text,
#         time text
#     )
# """

### create table for export info
create_table_export_info = """
    CREATE TABLE export_info (
        id integer,
        export_id integer,
        turn integer,
        pack text,
        scrap text,
        weight text,
        time text
    )
"""

# ### create table for export info
# create_table_export_info = """
#     CREATE TABLE export_info (
#         id integer,
#         export_id integer,
#         turn integer,
#         pack_id integer,
#         pack text,
#         scrap_id integer,
#         scrap text,
#         weight text,
#         time text
#     )
# """


### INSERT DATA TO TABLES
### insert to staff table
insert_to_staff = """
    INSERT INTO staff VALUES (
        00002,
        'Trần Văn B',
        'Xưởng cân',
        'Cân đầu vào',
        0123456789,
        '0',
        '0'
    )
"""

### insert to company table
insert_to_company = """
    INSERT INTO company VALUES (
        00002,
        'HUST',
        0123456789,
        '110110',
        'Dai Co Viet',
        'CT10105',
        '0',
        '0'
    )
"""

### insert to trucks table
insert_to_truck = """
    INSERT INTO truck VALUES (
        00002,
        00002,
        '88H8-5555',
        'Hyundai',
        '2000kg',
        'Lê Văn D',
        '090154545',
        '10002',
        '00:00',
        '00:00'
    )
"""
### insert to scrap table
insert_to_scrap = """
    INSERT INTO scrap VALUES (
        00002,
        'Sắt',
        '',
        'kg',
        '00:00',
        '00:00'
    )
"""

### insert into pack table
insert_to_pack = """
    INSERT INTO pack VALUES (
        00002,
        'Phuy 02',
        4.0,
        false,
        '00:00',
        '00:00'
    )
"""

# cursor.execute(create_table_staff)
# connection.commit()
# cursor.execute(create_table_company)
# connection.commit()
# cursor.execute(create_table_truck)
# connection.commit()
# cursor.execute(create_table_scrap)
# connection.commit()
# cursor.execute(create_table_pack)
# connection.commit()
# cursor.execute(create_table_import)
# connection.commit()
# cursor.execute(create_table_export)
# connection.commit()
# cursor.execute(create_table_export_info)
# connection.commit()

# cursor.execute(insert_to_staff)
# connection.commit()
# cursor.execute(insert_to_company)
# cursor.execute(insert_to_truck)
# cursor.execute(insert_to_scrap)
# cursor.execute(insert_to_pack)
# connection.commit()

# cursor.execute("DROP TABLE export")
# connection.commit()

connection.close()


