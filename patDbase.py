__author__ = "procoded"

import sqlite3

def PatRecData():
    con = sqlite3.connect("patRecords.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patRecords(id INTEGER PRIMARY KEY, patID text, Fullname text, DOB text, Gender text, Phone text, Mstatus text, Addy text, HInsurer text, PolID text,\
                ExDate text, Nationality text, Sname text, SAddy text, SPhone text, SRelate text, Famstory text, Medstory text, Medication text, Trestory text)")
    con.commit()
    con.close()


def addPatRec(patID, Fullname, DOB, Gender, Phone, Mstatus, Addy, HInsurer, PolID, ExDate, Nationality, Sname, SAddy, SPhone, SRelate, Famstory, Medstory, Medication, Trestory):
    con = sqlite3.connect("patRecords.db")
    cur = con.cursor(all)
    cur.execute("INSERT INTO patRecords VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",patID, Fullname, DOB, Gender, Phone, Mstatus, Addy, HInsurer, PolID, ExDate, \
                Nationality, Sname, SAddy, SPhone, SRelate, Famstory, Medstory, Medication, Trestory)
    con.commit()
    con.close()

def viewPatRec():
    con = sqlite3.connect("patRecords.db")
    cur = con.cursor(all)
    cur.execute("SELECT * FROM patRecords")
    rows = cur.fetchall()
    con.close()
    return rows

def deletePatRec(id):
    con = sqlite3.connect("patRecords.db")
    cur = con.cursor()
    cur.execute("DELETE FROM patRecords WHERE id = ?", (id,))
    con.commit()
    con.close()

def searchPatRec(patID = "", Fullname = "", DOB = "", Gender = "", Phone = "", Mstatus = "", Addy = "", HInsurer = "", PolID = "", ExDate = "", Nationality = "", Sname = "", SAddy = "",\
                 SPhone = "", SRelate = "", Famstory = "", Medstory = "", Medication = "", Trestory = ""):
    con = sqlite3.connect("patRecords.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patRecords WHERE patID=? OR Fullname=? OR DOB=? OR Gender=? OR Phone=? OR Mstatus=? OR Addy=? OR HInsurer=? OR PolID=? OR ExDate=? OR Nationality=? OR Sname=?\
                OR SAddy=? OR SPhone=? OR SRelate=? OR Famstory=? OR Medstory=? OR  Medication=? OR Trestory=?",(patID, Fullname, DOB, Gender, Phone, Mstatus, Addy, HInsurer, PolID, ExDate, \
                Nationality, Sname, SAddy, SPhone, SRelate, Famstory, Medstory, Medication, Trestory))
    rows = cur.fetchall()
    con.close()
    return rows

def updatePatRec(id, patID = "", Fullname = "", DOB = "", Gender = "", Phone = "", Mstatus = "", Addy = "", HInsurer = "", PolID = "", ExDate = "", Nationality = "", Sname = "", SAddy = "",\
                 SPhone = "", SRelate = "", Famstory = "", Medstory = "", Medication = "", Trestory =""):
    con = sqlite3.connect("patRecords.db")
    cur = con.cursor()
    cur.execute("UPDATE patRecords SET patID=?, Fullname=?, DOB=?, Gender=?, Phone=?, Mstatus=?, Addy=?, HInsurer=?, PolID=?, ExDate=?, Nationality=?, Sname=?,\
                SAddy=?, SPhone=?, SRelate=?, Famstory=?, Medstory=?,  Medication=?, Trestory=?",(patID, Fullname, DOB, Gender, Phone, Mstatus, Addy, HInsurer, PolID, ExDate, \
                Nationality, Sname, SAddy, SPhone, SRelate, Famstory, Medstory, Medication, Trestory, id))
    con.commit()
    con.close()




PatRecData()