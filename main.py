# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

read_table = pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql(
    """
    SELECT e.firstName, e.lastName 
    FROM employees e 
    JOIN offices o ON e.officeCode = o.officeCode 
    WHERE o.city = 'Boston';
""",
    conn,
)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql(
    """
    SELECT o.* 
    FROM offices o 
    LEFT JOIN employees e ON o.officeCode = e.officeCode 
    WHERE e.employeeNumber IS NULL;
""",
    conn,
)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql(
    """
    SELECT e.firstName, e.lastName, o.city, o.state 
    FROM employees e 
    LEFT JOIN offices o ON e.officeCode = o.officeCode 
    ORDER BY e.firstName ASC, e.lastName ASC;
""",
    conn,
)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql(
    """
    SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber 
    FROM customers 
    WHERE customerNumber NOT IN (SELECT customerNumber FROM orders) 
    ORDER BY contactLastName ASC;
""",
    conn,
)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql(
    """
    SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate 
    FROM customers c 
    JOIN payments p ON c.customerNumber = p.customerNumber 
    ORDER BY CAST(p.amount AS REAL) DESC;
""",
    conn,
)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql(
    """
    SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS num_customers 
    FROM employees e 
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
    GROUP BY e.employeeNumber 
    HAVING AVG(c.creditLimit) > 90000 
    ORDER BY num_customers DESC;
""",
    conn,
)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql(
    """
    SELECT p.productName, COUNT(od.orderNumber) AS numorders, SUM(od.quantityOrdered) AS totalunits 
    FROM products p 
    JOIN orderdetails od ON p.productCode = od.productCode 
    GROUP BY p.productCode 
    ORDER BY totalunits DESC;
""",
    conn,
)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql(
    """
    SELECT p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers 
    FROM products p 
    JOIN orderdetails od ON p.productCode = od.productCode 
    JOIN orders o ON od.orderNumber = o.orderNumber 
    GROUP BY p.productCode 
    ORDER BY numpurchasers DESC;
""",
    conn,
)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql(
    """
    SELECT COUNT(c.customerNumber) AS n_customers, o.officeCode, o.city 
    FROM offices o 
    JOIN employees e ON o.officeCode = e.officeCode 
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
    GROUP BY o.officeCode;
""",
    conn,
)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql(
    """
    SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode 
    FROM employees e 
    JOIN offices o ON e.officeCode = o.officeCode 
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
    JOIN orders ord ON c.customerNumber = ord.customerNumber 
    JOIN orderdetails od ON ord.orderNumber = od.orderNumber 
    WHERE od.productCode IN (
        SELECT p.productCode 
        FROM products p 
        JOIN orderdetails od2 ON p.productCode = od2.productCode 
        JOIN orders ord2 ON od2.orderNumber = ord2.orderNumber 
        GROUP BY p.productCode 
        HAVING COUNT(DISTINCT ord2.customerNumber) < 20
    )
    ORDER BY e.lastName ASC;
""",
    conn,
)

test_query = print(df_under_20[["employeeNumber", "firstName", "lastName"]])

conn.close()