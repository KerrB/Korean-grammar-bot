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
    content = q.readlines()
    n = 0
    while n < 3:
        quizWord = random.choice(content)
        Korean = re.search('([\u3131-\uD79D]*)', quizWord).group(1)
        English = re.search('([A-Z ]*[a-z ]+(\')*\s)+', quizWord).group(1)
        await ctx.message.author.send(Korean)
        print(English)
        try:
            message = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.message.author.send('Time is up! The correct answer was: ' + English.strip())
        else:
            if message.content.strip() == English.strip():
                await ctx.message.author.send('Correct!')
            else:
                await ctx.message.author.send('Incorrect. The correct answer was: ' + English.strip())
        n += 1

@client.command()
async def update(ctx):
    vocab_channel = client.get_channel(852701609132818534)
    message = await vocab_channel.history(limit=50).flatten()
    u = io.open("words.txt", 'a', encoding="utf-8")
    for msg in message:
        await ctx.message.author.send(msg.content)
        u.write(msg.content)
        u.write('\n')
        await asyncio.sleep(1.0)
        await vocab_channel.purge(limit=1)
        await asyncio.sleep(1.0)

@client.command()
async def jquiz(ctx):
    q = io.open('japanese.txt', 'r', encoding="utf-8")
    content = q.readlines()
    n = 0
    while n < 3:
        quizWord = random.choice(content)
        Japanese = re.search('([\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]*)', quizWord).group(1)
        English = re.search('([A-Z ]*[a-z ]+(\')*\s)+', quizWord).group(1)
        await ctx.message.author.send(Japanese)
        print(English)
        try:
            message = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.message.author.send('Time is up! The correct answer was: ' + English.strip())
        else:
            if message.content.strip() == English.strip():
                await ctx.message.author.send('Correct!')
            else:
                await ctx.message.author.send('Incorrect. The correct answer was: ' + English.strip())
        n += 1

@client.command()
async def jupdate(ctx):
    vocab_channel = client.get_channel(886796104593719356)
    message = await vocab_channel.history(limit=50).flatten()
    u = io.open("japanese.txt", 'a', encoding="utf-8")
    for msg in message:
        await ctx.message.author.send(msg.content)
        u.write(msg.content)
        u.write('\n')
        await asyncio.sleep(1.0)
        await vocab_channel.purge(limit=1)
        await asyncio.sleep(1.0)

client.run(TOKEN)


