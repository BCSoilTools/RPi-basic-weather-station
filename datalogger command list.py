import pandas as pd
import datetime

def current__init__():
    # building a dictionary for things I want to collect
    collectdf= {'datetime': ['yyyymmdd','20100210'], 
                'tempc': [22, 23], 
                'humidper': [50,60], 
                'pressurehpa': [1010, 1015]}
    # building the dataframe using pandas
    cstatus= pd.DataFrame(collectdf)
    return(cstatus)

print(current__init__())

def current__update__():
    