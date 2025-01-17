import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)
mycursor = mydb.cursor()
mycursor.execute("select*from product_table")
products=mycursor.fetchall()
print("Displaying all products:",products)
mydb.commit()
