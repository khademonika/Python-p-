import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="root", database="studentdb")
myCursor= mydb.cursor()
myCursor.execute("insert into studentInfo(name,surname,rollno) values('monika', 'khade', '109')")
mydb.commit()
print("data inserted")