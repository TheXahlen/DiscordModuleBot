import importlib
from discord.ext import commands
import discord
import yaml
import json
import functionlist
from functionlist import *
bot = discord.Client()

with open("bot.yaml") as yamlfile , open('commands.json') as jsonfile:
    watcher, jsondata =  yaml.load(yamlfile, Loader=yaml.FullLoader), json.load(jsonfile)

@bot.event
async def on_ready():
    print('READY\n VERSION 4.3\n Bot username is {}\n Bot id is {}\n Your command trigger is {}\n'.format(bot.user.name,bot.user.id,watcher["trigger"]))

bot.event
async def on_message(message):
    importlib.reload(functionlist)
    with open('commands.json') as jsonfile:
        jsondata = json.load(jsonfile)
        jsonfile.close()
        
    if (message.author == bot.user): pass     
    
    else: 
        
        if(message.content.lower()[0:len(watcher["trigger"])] == watcher["trigger"]):
            splitwhitespace = message.content[len(watcher["trigger"]) + 1:len(message.content)].lower().split(" ")
            returnkey = splitwhitespace[0]
            returnvalue = jsondata["commands"][splitwhitespace[0]]['value']
            returnparamater = jsondata["commands"][splitwhitespace[0]]['paramater']

            if returnvariable != "_": passedvariable = eval(locals()["returnvariable"])
            else: passedvariable = None
                
            if returnparamater != "NULL": passedparamater = returnparamater
            else: passedparamater = None

            testsendparam = [passedparamater, passedvariable]
            returntry = lambda testpart : testpart != None
            returntry = filter(returntry, testsendparam)
            pointeroflist = list(returntry)
            await message.channel.send(returnvalue.format(*pointeroflist))

        else: pass
        
bot.run(watcher["token"])
