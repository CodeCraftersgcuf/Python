import mysql.connector as c
con=c.connect(host="localhost",user="root",password="admin",database="amitdb")
if con.is_connected():
    print("Successfully Connected...")
else:
    print("Not Connected...")