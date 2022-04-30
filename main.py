import mysql.connector as mysql

#Connect to DB
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="Dontaskmeagain76",
    database="SchoolData"
)

mycursor = mydb.cursor()
mycursor = mydb.cursor(buffered=True)

while True:  
    #Main menu
    print("Main Menu")     
    print("Select one of the Options : ")   
    print(" press 1 : if you are a parent/legal guardian") 
    print(" press 2 : if you are a teacher")
    print(" press 3 : if you are a student") 
    theEnter = 1
    value = int(input("Enter: ")) 
    if value == 1:  
        print("Please enter you name: ")
        name = str(input("Enter: "))

        #This query is used to get student's data
        mycursor.execute(f"select * from Class where ParentName ='{name}'")
        myresult = mycursor.fetchall()
        studentID= 0
        studentName=""
        for x in myresult:
            studentID = x[0]
            studentName = x[1]

        print("What data would you like to acces?")
        print("press 1: for student data")
        print("press 2: for student grades")
        print("press 3: to create a view of your student's grades")
        newIn = int(input("Enter: "))
        if newIn == 1:
            for x in myresult:
                print(f"StudentID: {x[0]}")
                print(f"Name: {x[1]}")
        elif newIn == 2:
            #this query gets studen'ts grades and joins them with their data
            mycursor.execute(f"SELECT Class.StudentID, Class.StudentName, StudentGrades.History, StudentGrades.English, StudentGrades.Programming, StudentGrades.Math FROM Class INNER JOIN StudentGrades ON StudentGrades.StudentID = Class.StudentID;")
            myresult = mycursor.fetchall()
            for x in myresult:
                if x[0] == str(studentID):
                    print(f"StudentID: {x[0]}")
                    print(f"Name: {x[1]}")
                    print(f"History: {x[2]}")
                    print(f"English: {x[3]}")
                    print(f"Programming: {x[4]}")
                    print(f"Math: {x[5]}")
        elif newIn == 3:
            #this query create a view for the student's grades
            mycursor.execute(f"CREATE OR REPLACE VIEW grades AS SELECT StudentGrades.StudentID, StudentGrades.History, StudentGrades.English, StudentGrades.Programming, StudentGrades.Math from StudentGrades where studentID = '{studentID}';")
            mycursor.execute(f"select * from grades;")
            myresult = mycursor.fetchall()
            print(myresult)         
        else:
            print("Invalid input")

                
    elif value == 2:      
        teacher = input("Enter your teacher ID: ")
        mycursor.execute(f"select * from Teacher where teacherID ='{teacher}'")
        myresult = mycursor.fetchall()
        subject = ''
        for x in myresult:
            subject = x[1]
        student = input("Enter the name of the student you want to add a grade: ")
        mycursor.execute(f"select * from Class where StudentName ='{student}'")
        studentID = ''
        for x in myresult:
            studentID = x[0]

        mycursor.execute(f"select StudentGrades.{subject} from StudentGrades where StudentID ='{studentID}'")
        myresult = mycursor.fetchall()
        grades =''
        for x in myresult:
            grades = x[0]
        newGrade = input("What grade would you like to add? ")
        grades = grades+','+str(newGrade)
        mycursor.execute(f"UPDATE StudentGrades SET {subject} = '{grades}' WHERE StudentID = '{studentID}';")
        mycursor.execute(f"select StudentGrades.{subject} from StudentGrades where StudentID ='{studentID}'")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x[0])

    elif value== 3:  
        print("Please enter you name: ")
        name = str(input("Enter: "))
        mycursor.execute(f"select * from Class where StudentName ='{name}'")
        myresult = mycursor.fetchall()
        studentID= 0
        studentName=""
        for x in myresult:
            studentID = x[0]
            studentName = x[1]

        print("What data would you like to acces?")
        print("press 1: for student data")
        print("press 2: for student grades")
        print("press 3: to create a view of your student's grades")
        newIn = int(input("Enter: "))
        if newIn == 1:
            
            for x in myresult:
                print(f"StudentID: {x[0]}")
                print(f"Name: {x[1]}")
        elif newIn == 2:
            mycursor.execute(f"SELECT Class.StudentID, Class.StudentName, StudentGrades.History, StudentGrades.English, StudentGrades.Programming, StudentGrades.Math FROM Class INNER JOIN StudentGrades ON StudentGrades.StudentID = Class.StudentID;")
            myresult = mycursor.fetchall()
            for x in myresult:
                if x[0] == str(studentID):
                    print(f"StudentID: {x[0]}")
                    print(f"Name: {x[1]}")
                    print(f"History: {x[2]}")
                    print(f"English: {x[3]}")
                    print(f"Programming: {x[4]}")
                    print(f"Math: {x[5]}")
        elif newIn == 3:
            mycursor.execute(f"CREATE OR REPLACE VIEW grades AS SELECT StudentGrades.StudentID, StudentGrades.History, StudentGrades.English, StudentGrades.Programming, StudentGrades.Math from StudentGrades where studentID = '{studentID}';")
            mycursor.execute(f"select * from grades;")
            myresult = mycursor.fetchall()
            print(myresult)         
        else:
            print("Invalid input")
            
    wait = input("press any key to go to main menu: ") 