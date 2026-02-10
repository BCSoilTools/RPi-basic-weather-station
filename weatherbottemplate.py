import discord
import praw
import datetime
from discord.ext import commands
from discord.ext.commands import bot
import time
import smbus2
import bme280

# weather station initialization steps
port = 1
address = 0x76 #adjust to specific port used
bus = smbus2.SMBus(port)
params = bme280.load_calibration_params(bus, address)

#discord reddit bot functions
intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='&', intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel() #change to channel you want the message to relay to, 19 digit key
    print(channel)
    print('Logged on as', client.user)

@client.event
async def on_message(message):
    message.channel = client.get_channel() #change to channel you want the message to relay to, 19 digit key
    if message.content.startswith("&weather"):
        data = bme280.sample(bus, address, params)
        print("UTC", data.timestamp.strftime('%y-%m-%d - %H:%M'),
                                         "The current temperature is",
                                         round(data.temperature, 2))
        ctzone = "UTC" #current timezone
        ctime = data.timestamp.strftime('%y-%m-%d - %H:%M') #current time
        ctemp = round(data.temperature, 2) #current temperature
        chumid = round(data.humidity, 2) #current humidity
        cpress = round(data.pressure, 2) #current pressure
        # chunks to complete the sentence
        csentence = "The current temperature is"
        chsen = "humidity is"
        cpsen = "pressure is"
        cend = "degrees C"
        chend = "%"
        cpend = "hPa"
        await message.channel.send(f"{ctzone} {ctime} \n{csentence} {ctemp} {cend} \n{chsen} {chumid} {chend} \n{cpsen} {cpress} {cpend}")

##reddit API
#do take a look at instructions for PRAW package
client_id = "" #bot client id
client_secret = "" #bot secret key
username = "" #reddit bot username
password = "" #reddit bot password
user_agent = "postbot v1 by u/" #add your text here

reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, username = username, password = password, user_agent = user_agent)
subreddit = reddit.subreddit("") #select subreddit to post in

#discord API
# client = MyClient(intents=intents)
client.run('') #you need to add your discord bot key here. 
#to add bot to channel, build url in developer portal and use the url. Log in to your discord, it should prompt the rest

