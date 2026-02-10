import pandas as pd
import datetime
import os

# when building the system, the default sample collected is 5, as I am assuming I will be collecting at a 15 minute interval
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            collectdf=pd.read_csv(os.path.join(root, name))
            return(collectdf)
        else:
            collectdf= {'datetime': ['yyyymmdd','20100210', 'yyyymmdd','yyyymmdd','yyyymmdd',], 
                'tempc': [22, 23, 24, 23, 24], 
                'humidper': [50,60, 59, 55, 54], 
                'pressurehpa': [1010, 1015, 1009, 1011, 1012]} # initialize collection frame; this depends on frequency collected and storage limitations
            return(collectdf)

        

def current__init__(dirpath):
    # building a dictionary for things I want to collect
    os.chdir(dirpath) #set collection directory
    cwd=os.getcwd()
    collectdf=find("current_data.csv", cwd)
    # building the dataframe using pandas
    cstatus= pd.DataFrame(collectdf)
    cstatus.to_csv("current_data.csv", index=False) #building a repository in case loss of power, it can reinitiate
    return(cstatus)

print(current__init__("C:/Users/alanb/Desktop/discord bot test/weatherstation")) #add directory path here

def current__update__(datetime, temp, humid, pressure): 
