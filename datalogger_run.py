import smbus2
import bme280
import pandas as pd
import datetime
import os

# when building the system, the default sample collected is 5, as I am assuming I will be collecting at a 15 minute interval
def __init__(name, path):
    for root, dirs, files in os.walk(path): #in given file path
        if name in files: #if the name of the file matches
            collectdf=pd.read_csv(os.path.join(root, name)) #read the file (in this case, csv)
            return(collectdf)
        else:
            collectdf= {'datetime': ['yyyymmdd','20100210', 'yyyymmdd','yyyymmdd','yyyymmdd',], 
                'tempc': [22, 23, 24, 23, 24], 
                'humidper': [50,60, 59, 55, 54], 
                'pressurehpa': [1010, 1015, 1009, 1011, 1012]} # initialize collection frame; this depends on frequency collected and storage limitations
            a=54
            while a>0:
                collectdf['datetime'].append("time")
                collectdf['tempc'].append("temp")
                collectdf['humidper'].append("humid")
                collectdf['pressurehpa'].append("pres")
                a=a-1
            return(collectdf) #otherwise build the file

def current__init__(dirpath):
    # building a dictionary for things I want to collect
    os.chdir(dirpath) #set collection directory
    cwd=os.getcwd() #collect the name
    collectdf=__init__("current_data.csv", cwd) #find if datalogger csv file exists
    # building the dataframe using pandas
    cstatus= pd.DataFrame(collectdf) #turn into pandas dataframe
    cstatus.to_csv("current_data.csv", index=False) #building a repository in case loss of power, it can reinitiate
    return(cstatus)

#updating data as samples are taken
def current__update__(datetime, temp, humid, pressure, dirpath): 
    # building a dictionary for things I want to collect
    os.chdir(dirpath) #set collection directory
    cwd=os.getcwd()
    collectdf=__init__("current_data.csv", cwd) #read csv file needed to be updated
    # building the dataframe using pandas
    cstatus= pd.DataFrame(collectdf) #turn csv into pandas dataframe
    cstatus.drop(index=0, inplace=True) #oldest data is removed to maintain file size
    cstatus.loc[len(cstatus)+1]=[datetime, temp, humid, pressure] #sample data is added to csv
    cstatus.to_csv("current_data.csv", index=False) #building a repository in case loss of power, it can reinitiate
    return(cstatus)



alldatadir="/home/yard/Desktop" #add directory path here. comment this out when using the actual code, this is a test code
# collect data from sensor
port=1
address = 0x76
bus = smbus2.SMBus(port)
params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, params)
#turn sensor data into form to be integrated into csv file
ctime = data.timestamp.strftime('%y-%m-%d - %H:%M') #current time
ctemp = round(data.temperature, 2) #current temperature
chumid = round(data.humidity, 2) #current humidity
cpress = round(data.pressure, 2) #current pressure

cweather=current__update__(ctime,ctemp,chumid,cpress, alldatadir) #run update function
#print(cweather) #look at output in csv