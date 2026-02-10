exec(open('datalogger command list.py').read())
import smbus2
import bme280

alldatadir="/home/yard/Desktop" #add directory path here. comment this out when using the actual code, this is a test code
port=1
address = 0x76
bus = smbus2.SMBus(port)
params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, params)
ctime = data.timestamp.strftime('%y-%m-%d - %H:%M') #current time
ctemp = round(data.temperature, 2) #current temperature
chumid = round(data.humidity, 2)
cpress = round(data.pressure, 2)
cweather=current__update__(ctime,ctemp,chumid,cpress, alldatadir)
print(cweather)