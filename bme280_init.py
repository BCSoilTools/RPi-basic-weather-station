import smbus2
import bme280

#quick easy test to see if I2C connection is correct
port = 1
address = 0x76
bus = smbus2.SMBus(port)
params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, params)
print(data)