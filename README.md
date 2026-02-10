# RPi-basic-weather-station
A basic weather station that will log weather conditions, and do basic regression calculations and graphing

# Introduction
This tool is for hobbyists to build a simple monitoring system in their local environments. To collect local data and compare to more broadscale regional data, it will help visualize the difference between climate and microclimate differences. 
The initial reason for this existence come from finding a raspberry pi and trying to apply some learned technologies to use. This is absolutely not a tool for scientists to adapt into their research. 

This program uses discord as a proxy for relaying messages so it is essential to also read up on how to build and install discord bots. This will be included in the future if discord is still a viable route for this. reddit as well. 

# Requirements
hardware
- Raspberry Pi
- BME280 sensor (temp, humidity, pressure)
software
- python packages:
  - smbus2
  - bme280
  - datetime
  - discord (optional)
  - praw (optional)

# initialization
make sure you are able to upload scripts to the raspberry pi via usb or via VNC or SCP data transfer. 

Please follow instructions from https://pypi.org/project/RPi.bme280/ for initializing the raspberry pi for installing the sensor. below is an exerpt to help with it: 
1. Run sudo raspi-config
2. Use the down arrow to select 9 Advanced Options
3. Arrow down to A7 I2C
4. Select yes when it asks you to enable I2C
5. Also select yes when it asks about automatically loading the kernel module
6. Use the right arrow to select the <Finish> button
7. Select yes when it asks to reboot

once completed, use the pinout diagram of your RPI and the sensor to correctly link the power, data, clock, and ground together. 

run bme280_init.py to test if the sensor was correcly installed. (make that init file with simple commands)

# run program
for basic operations, it should be just as easy as running the weatherbot. the package should be able to run without messing around with much
NOTE: you will need to provide the bot with a couple of things: 
- a token for the discord bot
- an ID for your discord channel
- if using reddit:
  - client id
  - client secret
  - reddit username to log in to
  - reddit password
  - user agent (this is just a text that comes from the bot)
