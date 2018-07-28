import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print ("Running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def Saludos(ctx):
    await bot.say("""
    https://cdn.discordapp.com/attachments/381984341825290241/471890452803747841/FOTO_DE_LOS_AMIGOS.png"""), 
    print ("Saludos.")

client.loginprocess.env(NDcyNDg1OTIzNjI4NjQ2NDAx.Dj1YLA.PI15nAjip4dil67_3XWpqPrTHfA):
