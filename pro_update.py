import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)
mycursor = mydb.cursor()
product_to_update=input("Enter the product name to update price:")
new_price=float(input("Enter the new price:"))
mycursor.execute("update product_table set price = %s where product_name = %s",(new_price,product_to_update))
mydb.commit()
mycursor.execute("select * from product_table")
products=mycursor.fetchall()
print("Displaying products after price update:",products)
mycursor.close()
mydb.close()
