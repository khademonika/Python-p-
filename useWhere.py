import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="root", database="studentdb")
myCursor = mydb.cursor()
query = "select * from studentInfo where name = 'umesh'"
myCursor.execute(query)
res = myCursor.fetchall()
for x in res :
    print(x)
mydb.close()