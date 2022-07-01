import pandas as pd
import os
from os.path import isfile, join
from os import listdir
import re
from pathlib import Path
from datetime import datetime

landingPath = join(os.getcwd(), "landing")
dateset_file = Path(join(join(os.getcwd(), "dataset"),"price.csv"))

"""
find all dataset files
Assumption that only dataset files are dropped to this path and the dataset is in correct
DQA Check should be implemented if the quality of the dataset dropped to the folder cannot be ensured
"""

def Process_Data(newDataPath):
    #load data from path
    print(newDataPath)
    newData = pd.read_csv(newDataPath)
    print(newData)
    #remove rows with null/empty name
    
    newData = newData.dropna(subset = ['name'])

    #remove title from name
    titles = ['Ms', 'Mr', 'Miss', 'Dr', 'Mrs']
    regexTitle = r'\b(?:' + '|'.join(titles) + r')\.*\s*'
    newData['name_processed'] = newData['name'].str.replace(regexTitle, '')
    
    #Assumption the name is in first name, middle name, last name
    #Obtain first_name
    newData['first_name'] = newData['name_processed'].str.split(' ',n=1, expand=True).iloc[:, 0]
    #revers the splitted column to get the last value as last_name
    newData['last_name'] = newData['name_processed'].str.split(' ',n=-1, expand=True).iloc[:, ::-1].bfill(axis=1).iloc[:, 1]

    #Remove prepended Zeros and add column "above_100" set to 'true' when "price" > 100
    newData["price"] = pd.to_numeric(newData["price"], errors='coerce')
    newData.loc[newData['price'] > 100, 'above_100'] = 'true'

    #select required fields
    final = newData[["name","first_name", "last_name","price","above_100"]]
    return final

def Archive_File(newDataPath):
    os.rename(newDataPath, join(os.getcwd(), "landing/archive_ingested",newDataPath.split('\\')[-1]+'.'+datetime.now().strftime("%Y%m%d%H%M%S")))

for f in listdir(landingPath):
    if isfile(join(landingPath, f)):
        
        newProcessedData = Process_Data(join(landingPath, f))
        newProcessedData.to_csv(dateset_file, mode='a', index = False, header=not os.path.exists(dateset_file))
        Archive_File(join(landingPath, f))
        
