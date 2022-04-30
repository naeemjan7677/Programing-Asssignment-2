import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dontaskmeagain76",
    
)

mycursor = mydb.cursor()
mycursor.execute("create database SchoolData")

