#importing modules
from discord.ext import commands
import discord
import levels

cogs = [levels] #class system which allows modular design

client = commands.Bot[command_prefix='.', intents = discord.Intents.all()] #initiating a client

for i in range(len(cogs)): #to activate the cogs
    cogs[i].setup(client)
    print('Setup successful.')
    
client.run('token here') #the discord bot token from developer portal goes here
