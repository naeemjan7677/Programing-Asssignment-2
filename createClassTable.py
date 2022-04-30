#this class is used for creating the 
import mysql.connector
import csv 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dontaskmeagain76",
    database="SchoolData"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE Class (StudentID VARCHAR(255), \
    StudentName VARCHAR(255),\
    ParentName VARCHAR(255))")

except:
    pass

with open("class.csv", "r")as csvfile:
    csvdata = csv.reader(csvfile, delimiter=",")
    for row in csvdata:
        sql = "INSERT INTO Class VALUES (%s, %s ,%s)" # we insert the values to the table.
        val = (row[0], row[1], row[2])
        mycursor.execute(sql, val)
        mydb.commit()

mycursor.execute("select * from Class")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)