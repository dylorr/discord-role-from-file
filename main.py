
#imports
import discord
import asyncio
import nest_asyncio
nest_asyncio.apply()
from discord.ext import commands, tasks
from discord.utils import get
import pandas as pd
import time

#set and assign bot intents
intents = discord.Intents.default()
intents.members = True
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    #print('We have logged in as {0.user}'.format(client))
    guild = client.get_guild(enter server id here)
    role = discord.utils.get(guild.roles,name="enter role name here")

    #example of importing a csv, creating list from column of discord names, filtering out wrong names
    file= pd.read_csv('prewhitelist.csv')
    file_tolist = prewhitelist_file['col'].tolist()
    #filter our usernames w/o discriminator (#1234, etc.)
    file_tolist = [x for x in prewhitelist_list if '#' in x]
    #filter out usernames that start w/ a weird character
    file_tolist = [x.lstrip("!*@$") for x in prewhitelist_list]
    

    #loop through list of names
    for x in prewhitelist_list:
        try: 
            user = discord.utils.get(guild.members, name= x[:-5], discriminator= x[-4:]) #separate username from discriminator
            #add role to user, print success
            await user.add_roles(role)
            print(f'Succesfully added {role} to {user}')
            time.sleep(3)
        except AttributeError: 
            print(f'{x} was unable to be added to the role')

client.run('TOKEN')
