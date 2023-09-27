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

    mycursor = mydb.cursor()

    # Consume the result of SHOW DATABASES
    mycursor.execute("SHOW DATABASES")
    mycursor.fetchall()

    # Create database and switch to it
    mycursor.execute("CREATE DATABASE AltOnlineDB")
    mycursor.execute("USE AltOnlineDB")

    # Create table
    mycursor.execute("""
        CREATE TABLE department (
            department_title VARCHAR(255) PRIMARY KEY,
            child_department VARCHAR(255),
            description VARCHAR(255),
            FOREIGN KEY (child_department) REFERENCES department(department_title)
        )
    """)

    # Insert data
    sql = "INSERT INTO department (department_title, child_department, description) VALUES (%s, %s, %s)"
    data = ("TV", "Smart TV", "platt")
    mycursor.execute(sql, data)

    # Commit changes
    mydb.commit()

    mycursor.close()
    mydb.close()

except Exception as e:
    print("Error occurred:", e)
