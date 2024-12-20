import mysql.connector
mydb = mysql.connector.connect(host = "localhost", username="root", password="root" , database="studentdb")
mycursor = mydb.cursor()
mycursor.execute("create table studentInfo (name varchar(20), surname varchar(20), rollno int(10) primarykey)")
print('table created')