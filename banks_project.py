# Install required libraries: 
# in terminal: 
# pip install pandas, numpy, and bs4

# Download required exchanged rate file
# in terminal: 
# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv





# Code for ETL operations on Country-GDP data

# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 
from pprint import pprint
import os

# Define know entities
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billions"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'
exchange_rate_file = './exchange_rate.csv'

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
                data_dict = {"Name": col[1].find_all("a")[1]["title"],
                             "MC_USD_Billions": float(col[2].contents[0][:-1])}
                # Debugging: Print data_dict
                #pprint(data_dict)
    
                # Check if data_dict is empty
                if not data_dict["Name"] or not data_dict["MC_USD_Billions"]:
                    raise ValueError("Data dictionary is empty or improperly populated.")

                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
                #print(df)
    return df

#Read the exchange rate CSV file
exchange_rate_df = pd.read_csv('./exchange_rate.csv')

#Convert the contents to a dictionary
exchange_rate = dict(zip(exchange_rate_df.iloc[:, 0], exchange_rate_df.iloc[:, 1]))
#print(exchange_rate)

def transform(df):
  
#Add new columns to the DataFrame
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billions']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billions']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billions']]
    
    return df

###########################################################

def load_to_csv(df, csv_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(csv_path)

########################################################

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

##############################################################

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
 

#################################################################

# # ''' Here, you define the required entities and call the relevant
# # functions in the correct order to complete the project. Note that this
# # portion is not inside any function.'''

# #######################################################################

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

    ''' Here, you define the required entities and call the relevant 
    functions in the correct order to complete the project. Note that this
    portion is not inside any function.'''

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)

log_progress('Data extraction complete. Initiating Transformation process')

# print(df)

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

#print(df)

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('Banks.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, 'Largest_banks' )

log_progress('Data loaded to Database as table. Running the query')

run_query(f"SELECT * FROM Largest_banks", sql_connection)
run_query(f"SELECT AVG(MC_GBP_Billion) FROM Largest_banks", sql_connection)
run_query(f"SELECT Name from Largest_banks LIMIT 5", sql_connection)

log_progress('Process Complete.')

sql_connection.close()