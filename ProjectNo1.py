import mysql.connector
from speech_recognisation import get_voice_input 
mydb = mysql.connector.connect(
    host="localhost", username="root", password="root", database="StudentInfo"
)
mycursor = mydb.cursor()
print("Student Information")

def addingStudent():
    query1 = "insert into Studentinformation(name, surname, mobileno) values(%s,%s,%s) "
    name = input("Enter the name: ")              
    surname = input("Enter the surname: ")
    mobileno = input("Enter the Mobile Number: ")
    values = (name, surname, mobileno)
    mycursor.execute(query1, values)
    mydb.commit()


def showStudent():
    query2 = "select *from Studentinformation"
    mycursor.execute(query2)
    Data = mycursor.fetchall()
    for i in Data:
        print(i)
    mydb.commit()


def StudentByName():
    name = get_voice_input()
    query3 = "select * from Studentinformation WHERE name=%s "
    # inputName = input("Enter the name: ")
    values = (name,)
    mycursor.execute(query3, values)
    Data = mycursor.fetchall()
    for i in Data:
        print(i)
    # mydb.commit()


def StudentBySurname():
    query4 = "select * from Studentinformation WHERE surname=%s "
    name = get_voice_input()

    # inputName = input("Enter the Surname: ")
    values = (name,)
    mycursor.execute(query4, values)
    Data = mycursor.fetchall()
    for i in Data:
        print(i)
    mydb.commit()


def StudentByMobileNo():
    query5 = "select * from Studentinformation WHERE mobileno=%s "
    name = get_voice_input()

    # inputName = input("Enter the Mobile no.: ")
    values = (name,)
    mycursor.execute(query5, values)
    Data = mycursor.fetchall()
    for i in Data:
        print(i)
    mydb.commit()


def Update():
    query6 = "update studentinformation set name = %s, surname = %s, mobileno = %s where name = %s"
    inputName = input("Enter the Name: ")
    inputNamech = input("Enter the Name: ")
    Surname = input("Enter the Surname: ")
    Mobileno = input("Enter the Mobile no.: ")
    values = (inputName, inputNamech, Surname, Mobileno)
    mycursor.execute(query6, values)
    mydb.commit()


def delete():
    query7 = "delete from studentinformation where name = %s and surname = %s"
    inputName = input("Enter the Name: ")
    inputSurname = input("Enter the surname: ")
    values = (inputName, inputSurname)
    mycursor.execute(query7, values)
    mydb.commit()


def Exit():
    return ()


ans = "yes"
while ans == "yes":
    print("Choose One Option")
    print("1.Add New Student")
    print("2.Show all Students")
    print("3.Show student by Name")
    print("4.Show student by surname")
    print("5.Show student by Mobile no")
    print("6.Update Student")
    print("7.Delete Student")
    print("8.Exit")

    option = input("Enter the number  ")
    if option == "1":
      addingStudent()
      ans = input("Do you want to continue? yes/no ")

    elif option == "2":
      showStudent()
      ans = input("Do you want to continue? yes/no ")

    elif option == "3":
      StudentByName()
      ans = input("Do you want to continue? yes/no ")
       
    elif option == "4":
      StudentBySurname()
      ans = input("Do you want to continue? yes/no ")

    elif option == "5":
      StudentByMobileNo()
      ans = input("Do you want to continue? yes/no ")

    elif option == "6":
      Update()
      ans = input("Do you want to continue? yes/no ")
    elif option == "7":
      delete()
      ans = input("Do you want to continue? yes/no  ")

    elif option == "8":
      Exit()


