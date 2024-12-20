import mysql.connector

myDb= mysql.connector.connect(host ="localhost", username="root",password="root")
mycursor = myDb.cursor()
mycursor.execute("create database if not exists studentdb")
print("database created")

