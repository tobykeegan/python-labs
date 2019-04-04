import sqlite3
import os
import logging
logging.basicConfig(filename='errors.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
file_list = ["setup.py", "sqlite_setup.py", "database","data.txt"]

class Apprentice(object):

    data_source = "C:/Users/TobyKeegan/Documents/GitHub/python-labs/Introduction/data.txt"

    def __init__(self, name, age, base_location):

        self.name = name
        self.age = age
        self.base_location = base_location

        self.all_locations = [
            "South Bank", 
            "Portsmouth", 
            "South Harbour", 
            "Hursley", 
            "Other"
            ]

        self.all_departments = {
            "GBS": "Global Business Services",
            "GTS": "Global Technical Services", #might become redundant soon
            "Labs":"Cloud Services"
            }


def importNames():

    f = open(Apprentice.data_source, "r")
    data = f.read()
    names = data.split(",")

    for i in names:
        if "1" in i:
            print("Found invalid name, formatting %s" %(i))
            i = i.strip("1")
            print("New name value %s" %(i))

def fileCheck(filename):
    print("Checking ", filename)
    if os.path.isfile(filename) is False:
        raise FileNotFoundError
    else:
        print("File has been found")

print("Performing first time setup...")

for i in file_list:
    try:
        fileCheck(i)
        logging.info("File <%s> has been found" %(i))
    except FileNotFoundError:
        print("File <%s> has not been found." %(i))
        logging.error("File <%s> has not been found." %(i))
