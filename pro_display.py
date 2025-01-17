import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)
mycursor=mydb.cursor()
mycursor.execute("select * from product_table order by price")
products=mycursor.fetchall()
print("\nDisplaying products ordered by price:",products)
mycursor.close()
mydb.close()
