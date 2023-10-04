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

# Create database and switch to it
mycursor.execute("CREATE DATABASE ht23_1_project_group_42")
mycursor.execute("USE ht23_1_project_group_42")

#Task 3
# Create department table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
        department_title VARCHAR(255) PRIMARY KEY,
        parent_department VARCHAR(255),
        description VARCHAR(255),
        FOREIGN KEY (parent_department) REFERENCES department(department_title)
    )
""")

# Create homepage table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS homepage (
        welcome_text VARCHAR(255) PRIMARY KEY
    )
""")

# Create product table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        product_title VARCHAR(255) PRIMARY KEY,
        department_title VARCHAR(255),
        description VARCHAR(255),
        price INT,
        tax FLOAT,
        stock INT,
        sale FLOAT,
        featured BOOL,
        FOREIGN KEY (department_title) REFERENCES department(department_title)
    )
""")

# Create user table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        SSN INT PRIMARY KEY,
        email VARCHAR(255),
        password CHAR(64),
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        phone_number BIGINT,
        newsletter BOOL
    )
""")

# Create order table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS `order` (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        bought_quant INT,
        SSN INT,
        payment_reference BIGINT,
        status VARCHAR(255),
        date_of_last_changed DATETIME,
        date DATETIME,
        tracking_nr INT,
        FOREIGN KEY (SSN) REFERENCES user(SSN)
    )
""")

# Create address table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS address (
        SSN INT PRIMARY KEY,
        street_name VARCHAR(255),
        street_number INT,
        apartment_number VARCHAR(255),
        city VARCHAR(255),
        state VARCHAR(255),
        country VARCHAR(255),
        FOREIGN KEY (SSN) REFERENCES user(SSN)
    )
""")

# Create keyword table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS keywords (
        product_title VARCHAR(255),
        keyword VARCHAR(255),
        PRIMARY KEY (product_title, keyword),
        FOREIGN KEY (product_title) REFERENCES product(product_title)
    )
""")

# Create reviewed_by table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS reviewed_by (
        product_title VARCHAR(255),
        SSN INT,
        rating INT,
        text VARCHAR(255),
        FOREIGN KEY (product_title) REFERENCES product(product_title),
        FOREIGN KEY (SSN) REFERENCES user(SSN),
        PRIMARY KEY (product_title, SSN)
    )
""")

# Create listed_in table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS listed_in (
        product_title VARCHAR(255),
        order_id INT,
        FOREIGN KEY (product_title) REFERENCES product(product_title),
        FOREIGN KEY (order_id) REFERENCES `order`(order_id),
        PRIMARY KEY (product_title, order_id)
    )
""")

# Task 4: Inserting data

# Create at least 2 top-level departments, each having at least 3 child departments
departments_data = [
    ("Electronics", None, "Electronics Department"),
    ("Fashion", None, "Fashion Department"),
    ("Smartphones", "Electronics", "Smartphones Section"),
    ("Laptops", "Electronics", "Laptops Section"),
    ("Audio", "Electronics", "Audio Section"),
    ("Men", "Fashion", "Men's Clothing"),
    ("Women", "Fashion", "Women's Clothing"),
    ("Kids", "Fashion", "Kids' Clothing")
]

for data in departments_data:
    mycursor.execute("INSERT INTO department (department_title, parent_department, description) VALUES (%s, %s, %s)", data)

# Create at least 10 products in the store, some featured
products_data = [
    ("iPhone 13", "Smartphones", "Latest iPhone", 999, 0.2, 50, 0.1, True),
    ("MacBook Pro", "Laptops", "16 inch MacBook", 2399, 0.2, 30, None, False),
    ("Airpods Pro", "Audio", "Noise cancellation earbuds", 249, 0.2, 100, None, True),
    ("T-shirt", "Men", "Casual t-shirt", 20, 0.1, 200, None, False),
    ("Skirt", "Women", "Stylish skirt", 30, 0.1, 150, None, False),
    ("Jeans", "Men", "Regular fit jeans", 60, 0.1, 80, 0.2, False),
    ("Handbag", "Women", "Leather handbag", 120, 0.1, 40, None, True),
    ("Toy", "Kids", "Educational toy", 25, 0.1, 60, None, False),
    ("Dress", "Women", "Elegant dress", 150, 0.1, 20, 0.2, True),
    ("Headphones", "Audio", "Over-ear headphones", 300, 0.2, 25, None, False)
]

for data in products_data:
    mycursor.execute("INSERT INTO product (product_title, department_title, description, price, tax, stock, sale, featured) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", data)

# Create at least 2 users
users_data = [ 
    (123456789, "john@example.com", "hashed_password1", "John", "Doe", 1234567890, True),
    (987654321, "jane@example.com", "hashed_password2", "Jane", "Doe", 9876543210, False)
]

for data in users_data:
    mycursor.execute("INSERT INTO user (SSN, email, password, first_name, last_name, phone_number, newsletter) VALUES (%s, %s, %s, %s, %s, %s, %s)", data)

# Add their reviews for the same product (iPhone 13)
reviews_data = [
    ("iPhone 13", 123456789, 2, "I do not like this product, andriod GIGA CHAD. These iphone pheasants do not understand the value of customization."),
    ("iPhone 13", 987654321, 5, "Apple has changed the industry and we can all see why they are worth every penny!")
]

for data in reviews_data:
    mycursor.execute("INSERT INTO reviewed_by (product_title, SSN, rating, text) VALUES (%s, %s, %s, %s)", data)


# Create one order for one of the users (John)
order_data = [
    (123456789, 42, 819238717649832, "Confirmed", "2023-09-29 12:34:56", "2023-09-29 12:34:56", 111222)
]


for data in order_data:
    mycursor.execute("INSERT INTO `order` (SSN, bought_quant, payment_reference, status, date_of_last_changed, date, tracking_nr) VALUES (%s, %s, %s, %s, %s, %s, %s)", data)

# Get the last inserted order_id
mycursor.execute("SELECT LAST_INSERT_ID()")
order_id = mycursor.fetchone()[0]

# Add a product to that order (iPhone 13)
listed_in_data = [
    ("iPhone 13", order_id)
]

for data in listed_in_data:
    mycursor.execute("INSERT INTO listed_in (product_title, order_id) VALUES (%s, %s)", data)

#Task 5: SQL-queries

# Insert welcome text into homepage table
welcome_text = "Welcome to AltOnline AB, inspired by Amazon.com. We aim to become the market leader in online sales in Sweden."
mycursor.execute("INSERT INTO homepage (welcome_text) VALUES (%s)", (welcome_text,))

# Generate and insert keywords for products
keywords_data = [
    ("iPhone 13", "Apple"),
    ("iPhone 13", "smartphone"),
    ("iPhone 13", "iOS"),
    ("MacBook Pro", "Apple"),
    ("MacBook Pro", "laptop"),
    ("MacBook Pro", "macOS"),
    ("Airpods Pro", "Apple"),
    ("Airpods Pro", "earbuds"),
    ("Airpods Pro", "audio"),
    ("T-shirt", "clothing"),
    ("T-shirt", "casual"),
    ("T-shirt", "men"),
    ("Skirt", "clothing"),
    ("Skirt", "stylish"),
    ("Skirt", "women"),
    ("Jeans", "clothing"),
    ("Jeans", "regular fit"),
    ("Jeans", "men"),
    ("Handbag", "accessory"),
    ("Handbag", "leather"),
    ("Handbag", "women"),
    ("Toy", "children"),
    ("Toy", "educational"),
    ("Toy", "kids"),
    ("Dress", "clothing"),
    ("Dress", "elegant"),
    ("Dress", "women"),
    ("Headphones", "audio"),
    ("Headphones", "over-ear"),
    ("Headphones", "sound")
]

for data in keywords_data:
    mycursor.execute("INSERT INTO keywords (product_title, keyword) VALUES (%s, %s)", data)


# Fetch welcome text for homepage
mycursor.execute("SELECT welcome_text FROM homepage")
result = mycursor.fetchone()
print("Welcome text for homepage:", result[0])

# Fetch top-level departments for homepage
mycursor.execute("SELECT department_title, description FROM department WHERE parent_department IS NULL")
result = mycursor.fetchall()
print("Top-level departments for homepage:")
for row in result:
    print(row)

# Fetch featured products for homepage
mycursor.execute("SELECT product_title, description, price FROM product WHERE featured = TRUE")
result = mycursor.fetchall()
print("Featured products for homepage:")
for row in result:
    print(row)

# Fetch keyword-related products, assuming given product is 'iPhone 13'
given_product = 'iPhone 13'
mycursor.execute("""
SELECT p.product_title, p.description
FROM product p
JOIN keywords k1 ON p.product_title = k1.product_title
JOIN keywords k2 ON k1.keyword = k2.keyword
WHERE k2.product_title = %s AND k1.product_title != %s
""", (given_product, given_product))
result = mycursor.fetchall()
print(f"Keyword-related products for {given_product}:")
for row in result:
    print(row)

# Fetch products of a given department ('Smartphones') with their average rating
given_department = 'Smartphones'
mycursor.execute("""
SELECT p.product_title, p.description, p.price, AVG(r.rating) AS average_rating
FROM product p
LEFT JOIN reviewed_by r ON p.product_title = r.product_title
WHERE p.department_title = %s
GROUP BY p.product_title
""", (given_department,))
result = mycursor.fetchall()
print(f"Products in department {given_department} with average ratings:")

for row in result:
    print(row)

# Fetch all products on sale sorted by the discount percentage
mycursor.execute("""
SELECT product_title, price, sale
FROM product
WHERE sale IS NOT NULL
ORDER BY sale DESC
""")
result = mycursor.fetchall()
print("Products on sale sorted by discount:")
for row in result:
    print(row)

# Commit changes
mydb.commit()

# Close the cursor and connection
mycursor.close()
mydb.close()