import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)
mycursor=mydb.cursor()
product_to_delete=input("Enter the product name to delete: ")
mycursor.execute("Delete from product_table where product_name = %s",(product_to_delete,))
mydb.commit()
mycursor.execute("select*from product_table")
products = mycursor.fetchall()
print("\nDisplaying products after deletion:",products)
mydb.close()
