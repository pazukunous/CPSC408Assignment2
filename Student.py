import sqlite3
class Student:

    conn = sqlite3.connect('Students')
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Students(StudentId INTEGER PRIMARY KEY AUTOINCREMENT,FirstName VARCHAR(25) NOT NULL,LastName VARCHAR(25) NOT NULL,GPA NUMERIC NOT NULL ,Major VARCHAR(10) NOT NULL,FacultyAdvisor VARCHAR(25) NOT NULL)")

    def __init__(self, first_name, last_name, major, gpa, sid, facAdv):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.sid = sid
        self.facAdv = facAdv

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getMajor(self):
        return self.major

    def getGPA(self):
        return self.gpa

    def getSID(self):
        return self.sid

    def getFacAdv(self):
        return self.facAdv

    def getStudentTuple(self):
        return self.getFirstName(), self.getLastName(), self.getMajor(), self.getGPA(), self.getSID(), self.getFacAdv()
