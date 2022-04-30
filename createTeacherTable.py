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
    mycursor.execute("CREATE TABLE Teacher (teacherID VARCHAR(255), \
    Subject VARCHAR(255))")

except:
    pass

with open("teachers.csv", "r")as csvfile:
    csvdata = csv.reader(csvfile, delimiter=",")
    for row in csvdata:
        sql = "INSERT INTO Teacher VALUES (%s, %s)" # we insert the values to the table.
        val = (row[0], row[1])
        mycursor.execute(sql, val)
        mydb.commit()

mycursor.execute("select * from Teacher")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)