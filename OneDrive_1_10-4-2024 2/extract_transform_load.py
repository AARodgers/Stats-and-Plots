# Extract ,Transform, Load

# After completing this lab, you will be able to:

# Read CSV, JSON, and XML file types.
# Extract the required data from the different file types.
# Transform data to the required format.
# Save the transformed data in a ready-to-load format, which can be loaded into an RDBMS.

# Steps: 
# Download different file types in folder called source in the same folder your in
# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip

# Unzip the downloaded file ( in terminal)
#unzip source.zip

# Install pandas
# pip install pandas
# To install for specific python verion
# python3.11 -m pip install pandas

# Import necessary libraries
import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

# You also require two file paths that will be available globally in the code for all functions. 
# These are transformed_data.csv, to store the final output data that you can load to a database, and log_file.txt, that stores all the logs.
log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

# Write functions to extract data from each kind of file format

# Function to extract data from csv file
def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

# Function to extract data from json file (lines=True enables you to read the file as a JSON object on a line to line basis)
def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe 

# To extract XML file, you first need to parse data from file using ElementTree, then append it to dataframe
def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe 

# Function to identify which function to run on the file depending on its extension
def extract(): 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
     
    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

# Write function to transform data, note: the df is in form of a dictionary with three keys: name, height, weight
def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data 

#Load data to csv that can be loaded into a database
def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 

# Implement logging operation with message and timestamp
def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Test functions and log
# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 

# In terminal, execute file: pyton3 extract_transform_load.py