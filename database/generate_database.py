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
        measstaff text,
        collstaff text,
        pack text,
        type text,
        weight real,
        time text
    )
"""

### create table for export
create_table_export = """
    CREATE TABLE export (
        id integer,
        measstaff text,
        compname text,
        truck text,
        time text
    )
"""

### create table for export info
create_table_export_info = """
    CREATE TABLE export_info (
        id integer,
        exportid integer,
        turn id,
        pack text,
        scrap text,
        weight text,
        time text
    )
"""

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
        00001,
        'CTARG',
        0123456789,
        '110110',
        'C9-420',
        'CT10105',
        '0',
        '0'
    )
"""

### insert to trucks table
insert_to_truck = """
    INSERT INTO truck VALUES (
        00001,
        00001,
        '88H8-8888',
        'Thaco',
        '5000kg',
        'Trần Văn B',
        '0901541688',
        '10001',
        '00:00',
        '00:00'
    )
"""
### insert to scrap table
insert_to_scrap = """
    INSERT INTO scrap VALUES (
        20001,
        'Nhôm vụn',
        'Do phay nhôm',
        'kg',
        '00:00',
        '00:00'
    )
"""

### insert into pack table
insert_to_pack = """
    INSERT INTO pack VALUES (
        30001,
        'Thùng 01',
        2.0,
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

# cursor.execute("DROP TABLE import")
# connection.commit()

connection.close()


