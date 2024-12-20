import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", username="root", password="root", database="studentdb"
)
myCursor = mydb.cursor()
query = "insert into studentInfo(name, surname, rollno) values(%s, %s, %s)"

name = input("Enter your name: ")
surname = input("Enter your surname: ")
rollno = input("Enter your rollno: ")
myCursor.execute(query, (name, surname, rollno))
mydb.commit()
mydb.close()
