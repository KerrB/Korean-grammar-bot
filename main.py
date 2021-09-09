# bot.py
import os

import re
import io
import random

import asyncio

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
    q = io.open('words.txt', 'r', encoding="utf-8")
    await ctx.message.author.send('put greeting and instructions here')
    content = q.readlines()
    quizWord = random.choice(content)
    Korean = re.search('([\u3131-\uD79D]*)', quizWord).group(1)
    English = re.search('([A-Z]*[a-z]+(\')*\s)+', quizWord).group(1)
    await ctx.message.author.send(Korean)
    print(English)
    try:
        message = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.message.author.send('Time is up!')
    else:
        if message.content() == English:
            await ctx.message.author.send('Correct!')
        else:
            await ctx.message.author.send('That was incorrect')

@client.command()
async def update(ctx):
    vocab_channel = client.get_channel(852701609132818534)
    message = await vocab_channel.history(limit=1).flatten()
    u = io.open("words.txt", 'a', encoding="utf-8")
    for msg in message:
        await ctx.message.author.send(msg.content)
        u.write(msg.content)
        u.write('\n')

client.run(TOKEN)


