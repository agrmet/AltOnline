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
        password=mysql_password,
        database="AltOnlineDB"
    )
    print("MySQL connection established.")

    mycursor = mydb.cursor()

    # Fetch all table names in the database
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()

    # Describe the structure of each table
    print("Table Structures:")
    for table in tables:
        table_name = table[0]
        print(f"\nStructure of {table_name}:")
        mycursor.execute(f"DESCRIBE {table_name}")
        for x in mycursor:
            print(x)

    # Fetch data from each table
    print("\nTable Data:")
    for table in tables:
        table_name = table[0]
        print(f"\nData in {table_name}:")
        mycursor.execute(f"SELECT * FROM {table_name}")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    mycursor.close()
    mydb.close()

except Exception as e:
    print("Error occurred:", e)
