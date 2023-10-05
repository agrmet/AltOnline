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

product_title = input("Enter product title:")

def get_discount(product_title_arg):
    mycursor.execute("""
                        SELECT sale
                        FROM product 
                        WHERE product_title = '{product}'
                        """.format(
        product=product_title_arg))

    discount = mycursor.fetchall()

    for x in discount:
        print(f"Discount for {product_title_arg} is : {x[0]}")
get_discount(product_title)

change_discount = input("Do you want to change the discount?(Y/n):")
if(change_discount.lower() == "y"):
    new_discount = input("What is the new discount?:")
    mycursor.execute("""
                     UPDATE product
                     SET sale = '{discount}'
                     WHERE product_title = '{product}'
    """.format(
        discount=new_discount, product=product_title
    ))
    get_discount(product_title)


mydb.commit()

mycursor.close()
mydb.close()