# In order to work MySQL with Python, you need to install the MySQL Connector/Python driver.
# You can install it using pip3:
# pip3 install mysql-connector-python
# Import the MySQL Connector module
# This program willconnect to MySQL server and fetch the table data from the lassicmodels.employees table
# and write the output to a file called employees.txt
# Import the MySQL Connector module
import mysql.connector

# Open database connection
db = mysql.connector.connect(
    host="localhost", user="root", password="Macbook!981")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
if data:
    print('Version available: ', data)
else:
    print('Version not retrieved.')
fout = open('employees.txt', 'w')  # to write the output file
# Fetch data from classicmodels.employees
cursor.execute("SELECT * FROM classicmodels.employees")

myresult = cursor.fetchall()

for x in myresult:
    print(x)
    fout.write(str(x) + '\n')  # write to the file
fout.write('....\n')
fout.close()
# disconnect from server
db.close()
