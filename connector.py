import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS stu1")
mycursor.execute("create table stu1(sid int, sname varchar(20))")
print("Table 'stu1' created successfully")
insert="insert into stu1(sid,sname) values(%s, %s)"
values=(1,"deekshi")
mycursor.execute(insert,values)
mydb.commit()
print("Data inserted successfully.")
update="update stu1 set sname=%s where sid=%s"
update_values=("deekshitha",1)
mycursor.execute(update, update_values)
mydb.commit()
print("Data updated successfully.")
