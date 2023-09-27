import mysql.connector
#prutt

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

    mycursor = mydb.cursor() #create a cursor object
    mycursor.execute("SHOW DATABASES")
    mycursor.execute("CREATE DATABASE AltOnlineDB") #creation of DB
    mycursor.execute("USE AltOnlineDB") #"Switching" to DB

    # Start creating tables
    mycursor.execute("""
            CREATE TABLE department (
                    department_title VARCHAR(255) PRIMARY KEY,
                    child_department VARCHAR(255),
                    descritption VARCHAR(255),
                    FOREIGN KEY (child_department) REFERENCES department(departname_name)
            )
        """)
    #specifying in what order data populates
    sql = "INSERT INTO department (department_title, child_department, description) VALUES (%s, %s, %s)"
    
    #the data that is populated into the table
    data = ("TV", "Smart TV", "platt")

    #go through each row
    # for val in data:
    mycursor.execute(sql,data)

    mydb.commit()

    for x in mycursor:
        print(x)

    mycursor.close()
    mydb.close()


except Exception as e:
    print("Error occurred:", e)