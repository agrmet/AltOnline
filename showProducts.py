import mysql.connector

try:
    # MySQL credentials
    mysql_username = "ht23_1_group_42"
    mysql_password = "pasSWd_42"
    mysql_host = "fries.it.uu.se"

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host=mysql_host,
        user=mysql_username,
        password=mysql_password
    )
    print("MySQL connection established.")
except Exception as e:
    print("Error occurred:", e)
    exit(1)  # Exit if connection is unsuccessful

mycursor = mydb.cursor()

mycursor.execute("USE ht23_1_project_group_42")

department_id = input("Enter a department:")



mycursor.execute("""SELECT parent_department
                 FROM department
""")

parent_dps = mycursor.fetchall()

if((department_id,) in parent_dps):
    mycursor.execute(""" 
                        SELECT department_title
                        FROM department
                        WHERE parent_department = '{department}'
                        """.format(
    department=department_id))
    result = mycursor.fetchall()
    for row in result:
        print(f"Sub-Department: {row[0]}")
else:
    mycursor.execute("""
                    SELECT product_title, price, tax, sale
                    FROM product 
                    WHERE department_title = '{department}'
                    """.format(
    department=department_id))
    result = mycursor.fetchall()
    for row in result:
        print(f"Product:{row[0]} Price:{round((row[1]+row[1]*row[2])*(1-0.2))}")
    




mycursor.close()
mydb.close()