import discord
import praw
import datetime
from discord.ext import commands
from discord.ext.commands import bot
import time
import smbus2
import bme280
import pandas as pd
import os

#data directory
alldatadir="/home/yard/Desktop" #add directory path here. comment this out when using the actual code, this is a test code

# weather station initialization steps
port = 1
address = 0x76
bus = smbus2.SMBus(port)
params = bme280.load_calibration_params(bus, address)

#discord reddit bot functions
intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='&', intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel()
    print(channel)
    print('Logged on as', client.user)

@client.event
async def on_message(message):
    message.channel = client.get_channel()
    if message.content.startswith("&weather"):
        data = bme280.sample(bus, address, params)
        #print("UTC", data.timestamp.strftime('%y-%m-%d - %H:%M'),
                                         #"The current temperature is",
                                         #round(data.temperature, 2))
        ctzone = "UTC" #current timezone
        ctime = data.timestamp.strftime('%y-%m-%d - %H:%M') #current time
        ctemp = round(data.temperature, 2) #current temperature
        chumid = round(data.humidity, 2)
        cpress = round(data.pressure, 2)
        csentence = "The current temperature is"
        chsen = "humidity is"
        cpsen = "pressure is"
        cend = "degrees C"
        chend = "%"
        cpend = "hPa"
        await message.channel.send(f"{ctzone} {ctime} \n{csentence} {ctemp} {cend} \n{chsen} {chumid} {chend} \n{cpsen} {cpress} {cpend}")
        # temporary code for checking datalogging capabilities
        collectdf=pd.read_csv(os.path.join(alldatadir, "slope_data.csv")) #read the file (in this case, csv)
        trendmessage="In the last hour, "
        if collectdf["tempc"][0]>0.01:
            trendtemp="The temperature is increasing"
        elif collectdf["tempc"][0]<-0.01:
            trendtemp="the temperature is decreasing"
        else:
            trendtemp="The temperature is stable"
        if collectdf["humidper"][0]>0.01:
            trendhum="The humidity is increasing"
        elif collectdf["humidper"][0]<-0.01:
            trendhum="the humidity is decreasing"
        else:
            trendhum="The humidity is stable"
        if collectdf["pressurehpa"][0]>0.01:
            trendpres="The pressure is increasing"
        elif collectdf["humidper"][0]<-0.01:
            trendpres="the pressure is decreasing"
        else:
            trendpres="The pressure is stable"
        await message.channel.send(f"{trendmessage} {trendtemp} \n{trendhum} \n{trendpres} ")

##reddit API
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = "postbot v1 by u/"

reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, username = username, password = password, user_agent = user_agent)
subreddit = reddit.subreddit("datsurreyboi")


#discord API
# client = MyClient(intents=intents)
client.run('')
#to add bot to channel, use the provided url and login to your discord, it should prompt the rest


#OBS API
#cl = obs.ReqClient(host='', port=, password='', timeout=3)
#resp = cl.get_version()
#print(f"OBS Version: {resp.obs_version}")
#cl.start_stream()
#cl.stop_stream()