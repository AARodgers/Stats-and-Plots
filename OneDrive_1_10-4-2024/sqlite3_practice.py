# Querying sqlite3 database

# Connect to sqlite3
# import sqlite3
# sql_connection = sqlite3.connect(‘database.db’)

# Load a pandas df into sqlite3 object
# df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)
# note:
# The if_exists parameter can take any one of three possible values:
# 'fail': This denies the creation of a table if one with the same name exists in the database already.
# 'replace': This overwrites the existing table with the same name.
# 'append': This adds information to the existing table with the same name.
# Keep the index parameter set to True only if the index of the data being sent holds some informational value. Otherwise, keep it as False.

# Query a database table using sqlite3 and pandas
# df = pandas.read_sql(query_statement, sql_connection)

# Lab
# In this lab you'll learn how to:

# Create a database using Python

# Load the data from a CSV file as a table to the database

# Run basic "queries" on the database to access the information

# Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :

# Header	Description
# ID	Employee ID
# FNAME	First Name
# LNAME	Last Name
# CITY	City of residence
# CCODE	Country code (2 letters)

# terminal: 
# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv

# make sure pandas is installed

import sqlite3
import pandas as pd

# use SQLite3 to create and connect your process to a new database
conn = sqlite3.connect('STAFF.db') 

# Create the table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Read the CSV
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

#Load the data to the table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

# Do a query on the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# View only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# View total number of entries in table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Append data to table (first create a dictionary to create a df of new data)
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# Append the data to the Instructor table
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Run count query again to see if above worked
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Make sure to close connection to db
conn.close()

# execute script/file in terminal:
# python3 sqlite3.py 