import mysql.connector

mydb = mysql.connector.connect(host = "localhost", username="root", password="root", database="studentdb")
myCursor = mydb.cursor()
query = "update studentInfo set name = 'Umesh' where name = 'Khushi' "
myCursor.execute(query)
mydb.commit()