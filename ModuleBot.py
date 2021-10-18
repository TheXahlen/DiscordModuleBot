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

@bot.event
async def on_message(message):
    await bot.change_presence(activity=discord.Game('Greeting Goofy Yellow Men'))
    print("hello")
    print(watcher["trigger"])
    importlib.reload(functionlist)
    with open('commands.json') as jsonfile:
        json_data = json.load(jsonfile)
        jsonfile.close()

    if (message.author == bot.user): pass

    else:

        if(message.content.lower()[0:len(watcher["trigger"])] == watcher["trigger"]):
            split_whitespace = message.content[len(watcher["trigger"]) + 1:len(message.content)].lower().split(" ")
            command_type = json_data["commands"][split_whitespace[0]]
            return_key = split_whitespace[0]
            return_value = command_type['value']
            return_paramater = command_type['paramater']
            return_variable = eval("jsondata['commands'][split_whitespace[0]]['variable']")
            if return_variable != "_":
                passed_variable = eval(locals()["return_variable"])
            else:
                passed_variable = None
            if return_paramater != "NULL":
                passed_paramater = return_paramater
            else:
                passed_paramater = None
            test_sendparam = [passed_paramater, passed_variable]
            return_try = lambda test_part : test_part != None
            return_try = filter(return_try, test_sendparam)
            pointer_oflist = list(return_try)

            await message.channel.send(return_value.format(*pointer_oflist))

bot.run(watcher["token"])
