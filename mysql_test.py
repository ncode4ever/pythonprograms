# ========================================
# MySQL Database Connection and Data Export
# ========================================
# In order to work MySQL with Python, you need to install the MySQL Connector/Python driver.
# You can install it using pip3:
# pip3 install mysql-connector-python
#
# This program connects to a MySQL server, retrieves employee data from the classicmodels.employees
# table, checks the MySQL version, and exports all data to a file called employees.txt

import os
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========================================
# Connection Setup
# ========================================
# Retrieve MySQL password from environment variable for secure credential handling
mysql_password = os.environ.get('MYSQL_PASSWORD')

# Establish connection to MySQL server using credentials
# host: MySQL server address
# user: database user (root in this case)
# password: retrieved from environment variable
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_password
)

# Create a cursor object to execute SQL queries
# The cursor acts as an intermediary between Python and the MySQL server
cursor = db.cursor()

# ========================================
# Database Version Check
# ========================================
# Execute SQL query to retrieve the current MySQL server version
cursor.execute("SELECT VERSION()")

# Fetch the first row from the query result using fetchone() method
data = cursor.fetchone()

# Display the MySQL version if available
if data:
    print('Version available: ', data)
else:
    print('Version not retrieved.')

# ========================================
# Data Export Section
# ========================================
# Open a file named 'employees.txt' in write mode to store the exported data
fout = open('employees.txt', 'w')

# Execute query to fetch all employee records from the classicmodels database
cursor.execute("SELECT * FROM classicmodels.employees")

# Fetch all rows from the query result using fetchall() method
# This stores all records as a list of tuples
myresult = cursor.fetchall()

# Iterate through each employee record
for x in myresult:
    # Display the employee record in the console
    print(x)
    # Write each record as a string to the output file on a new line
    fout.write(str(x) + '\n')

# Write a separator line to mark the end of data in the file
fout.write('....\n')

# Close the output file to ensure all data is written
fout.close()

# ========================================
# Email Configuration and Sending
# ========================================
# Email credentials and configuration
sender_email = "narayan.shegde@gmail.com"  # Change to your email address
recipient_email = "narayan.shegde@gmail.com"  # Change to recipient's email
# Retrieve password from environment variable
# Ensure you set this environment variable before running the program
email_password = os.environ.get('EMAIL_PASSWORD')
print(email_password)

# Check if email password is set
if not email_password:
    print("Error: EMAIL_PASSWORD environment variable not set.")
    print("Please set it using: export EMAIL_PASSWORD='your-password'")
    # exit(1)

print(email_password)
# Email subject
email_subject = "MySQL Employee Data Export"

# Read the employees.txt file to include in email body
try:
    with open('employees.txt', 'r') as file:
        email_body = file.read()

    # Create a multipart email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = email_subject

    # Attach the email body
    message.attach(MIMEText(email_body, 'plain'))

    # Send the email via Gmail SMTP server
    print("Attempting to send email...")
    # Gmail SMTP server with SSL
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, email_password)  # Login to Gmail account
    server.sendmail(sender_email, recipient_email,
                    message.as_string())  # Send the email
    server.quit()  # Close the connection
    print(f"Email sent successfully to {recipient_email}!")

except FileNotFoundError:
    print("Error: employees.txt file not found.")
except smtplib.SMTPAuthenticationError:
    print("Error: Email authentication failed. Check your email address and password.")
except smtplib.SMTPException as e:
    print(f"Error: Failed to send email. {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")

# ========================================
# Cleanup
# ========================================
# Disconnect from the MySQL server to release the connection
db.close()
