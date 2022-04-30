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
    mycursor.execute("CREATE TABLE StudentGrades (StudentID VARCHAR(255), \
    English VARCHAR(255),\
    History VARCHAR(255), \
    Programming VARCHAR(255),\
    Math VARCHAR(255),\
    PRIMARY KEY (StudentID))") #we need pk to be able to edit this table

except:
    pass

with open("studentGrades.csv", "r")as csvfile:
    csvdata = csv.reader(csvfile, delimiter="/") #used the / delimiter in order to be able to use , when i list the grades
    
    for row in csvdata:
        sql = "INSERT INTO StudentGrades VALUES (%s, %s ,%s, %s ,%s)" 
        val = (row[0], row[1], row[2], row[3], row[4])
        mycursor.execute(sql, val)
        mydb.commit()

mycursor.execute("select * from StudentGrades")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)