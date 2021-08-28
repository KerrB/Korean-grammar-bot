# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    channel = client.get_channel(793640270355890176)
    await channel.send('Korean Bot has connected to the server')

@client.command()
async def quiz(ctx):
    channel = client.get_channel(852701609132818534)
    message = await channel.history(limit=200).flatten()
    await ctx.message.author.send(message)

client.run(TOKEN)


