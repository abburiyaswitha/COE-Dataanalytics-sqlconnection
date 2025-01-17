import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)
mycursor=mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS product_table")
mycursor.execute("create table product_table(product_id int, product_name varchar(50), price decimal(10, 2))")
num_products=int(input("Enter the number of products to insert: "))
for _ in range(num_products):
    product_id=int(input("Enter product ID:"))
    product_name=input("Enter product name:")
    price=float(input("Enter product price:"))
    mycursor.execute("insert into product_table(product_id, product_name,price) values(%s, %s, %s)", (product_id, product_name, price))
mydb.commit()

