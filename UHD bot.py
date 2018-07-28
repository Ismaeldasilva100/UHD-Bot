import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

client = discord.Client()

worker:node UHD bot.py

@client.event
async def on_ready():
    print ("active")

@client.event
async def on_message(message):
    if message.content.upper().startswith('$RALLY'):
        if '472491647410765825' in [role.id for role in message.author.roles]:
            await client.send_message(message.channel,"@here Combat training! https://www.roblox.com/games/328934678/tryhardedgelordtops?privateServerLinkCode=7SsDxo7esTneqFXn-UN18uu60tcTchnE")
        else:
            await client.send_message("You can't do that!")
    elif message.content.upper().startswith('$STARTUP'):
        if '472491647410765825' in [role.id for role in message.author.roles]:
            await client.send_message("@here Server startup at NH! https://www.roblox.com/games/1805065726/UNSC-New-Harmony")
        else:
           await client.send_message(message.channel,"You can't do that!")
    elif message.content.upper().startswith('$VERSION'):
        embed = discord.Embed(title="Current Version:", description="0.0.2", color=0xbc6434)
        await client.send_message(message.channel,embed=embed)
    elif message.content.upper().startswith('$CREDITS'):
        embed = discord.Embed(title="Credits:", description="""
Creator: Ism""", color=0xbc6434)
        await client.send_message(message.channel,embed=embed)
    elif message.content.upper().startswith('$HELP'):
        embed = discord.Embed(title="Current Commands:", description="""
- $Help
- $Version
- $Credits
**Admin Commands**
- $Startup
- $Rally""", color=0xbc6434)
        await client.send_message(message.channel, embed=embed)

client.loginprocess.env(NDcyNDg1OTIzNjI4NjQ2NDAx.Dj1YLA.PI15nAjip4dil67_3XWpqPrTHfA):
