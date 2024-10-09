# Task:
# From this website: https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films
# Get the Average Rnad, Film, and Year
# Write pyton script that extracts the info to a csv file ( top_50_films.csv) and save to db (Movies.db) under table Top_50
# Libraries: 
# You require the following libraries for this lab.

# pandas library for data storage and manipulation.

# BeautifulSoup library for interpreting the HTML document.

# requests library to communicate with the web page.

# sqlite3 for creating the database instance.
# While requests and sqlite3 come bundled with Python3, you need to install pandas and BeautifulSoup (bs4) libraries 
# Terminal: pip install pandas
# pip install bs4

# Import libraries
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Initialize known entities
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/mnt/c/Users/Amanda.Rodgers/OneDrive - Voyatek/Code/python_data_science/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# Load webpage as HTML document in python and parse text using BeautifulSoup
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Define rows using beautiful soup object
# Finds all tables
tables = data.find_all('tbody')
# Finds all rows of first table
rows = tables[0].find_all('tr')

# Iterate over rows to get the data
for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

# Print contents of df
print(df)

# Save df to csv file
df.to_csv(csv_path)

# To store data in database, first initialize a connection to db, save df as table and the close connection
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

# Run the file
# In terminal: python3 web_scraping_api.py