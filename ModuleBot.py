import importlib
from discord.ext import commands
import discord
import yaml
import json
import functionlist
from functionlist import *

##defines a bot class within the discord.py libary
bot = discord.Client()
variablepassed = False
        
##This checks if the config file is defined. 
## This file should be called bot.yaml, with the folling defined.
## trigger : "" >>> this is what you want as a trigger for the bots commands 
## token : "" >>> this is for your discord api token
with open("bot.yaml") as yamlfile:
    watcher = yaml.load(yamlfile, Loader=yaml.FullLoader)
    yamlfile.close()
trigger = watcher["trigger"]

with open('commands.json') as jsonfile:
    jsondata = json.load(jsonfile)
    jsonfile.close()

@bot.event
async def on_ready():
    print('READY\n VERSION 4.3\n Bot username is {}\n Bot id is {}\n Your command trigger is {}\n'.format(bot.user.name,bot.user.id,trigger))
##This function runs on every message send.
    
@bot.event
async def on_message(message):
    importlib.reload(functionlist)
    with open('commands.json') as jsonfile:
        jsondata = json.load(jsonfile)
        jsonfile.close()
    #Simple list of commands by using a dictionary, the key is the command and the value is what is returned or ran, "RAN" as in you can run a function when given a keypair
    # this can allow you to update variables or check text files if you are logging users etc, after which you can return, what ever is used in the return is what's sent
    #in the message.    
    ## very important piece of code, without this the bot registers it's own messages and sends a response.
    if (message.author == bot.user): pass      
    else: 
        ## This is a check to see if your trigger word or symbol is the first half of the message if it isn't it just won't continue.
        if(message.content.lower()[0:len(trigger)] == trigger):
            #this splits based on white space after parsing everything other than the trigger. 
            splitwhitespace = message.content[len(trigger) + 1:len(message.content)].lower().split(" ")
            #This is a check to see if there are any paramaters passed, by splitting the message by it's whitespace, allowing the bot to chek if there is more than 
            #one paramater.
            returnkey = splitwhitespace[0]
            returnvalue = jsondata["commands"][splitwhitespace[0]]['value']
            returnparamater = jsondata["commands"][splitwhitespace[0]]['paramater']
            returnvariable = eval("jsondata['commands'][splitwhitespace[0]]['variable']")
            
            
            ## These assign a None if they aren't passed so the message knows it doesn't need to use them
            ## in the format function
            print(locals()["returnvariable"])
            if returnvariable != "_": passedvariable = eval(locals()["returnvariable"])
            else: passedvariable = None
            
            if returnparamater != "NULL": passedparamater = returnparamater
            else: passedparamater = None
            #debugging print("paramater passed {%s}" % returnparamater)
            #debugging print("variable passed {%s}" % passedvariable)

            ##this tests to see if things have been passed and sends the message if they have
            ##It formats the message as needed, to what ever it could need
            testsendparam = [passedparamater, passedvariable]
            returntry = lambda testpart : testpart != None
            returntry = filter(returntry, testsendparam)
            pointeroflist = list(returntry)
            await message.channel.send(returnvalue.format(*pointeroflist))

            
        
        ##This is a simple pass function that just ends the attempt to read a command if it has determined there is no
        ##trigger word, phrase, or sybmol in the begging substring of the message.
        else: pass
        
##starts up bot using token from bot.yaml file
bot.run(watcher["token"])