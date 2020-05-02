import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from functools import reduce

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

assert TOKEN, "A token is required"

current_totals = {}

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def registerme(ctx):
    author = ctx.message.author
    if author not in current_totals:
        current_totals[author] = 0
    await ctx.send(f'I have you registered with ${current_totals[author]}.')

@bot.command()
async def showtotals(ctx):
    totals = reduce(lambda x, y: x + f"\n{y[0]}: ${y[1]}",  current_totals.items(), "")
    await ctx.send(totals)

@bot.command()
async def addmoney(ctx, amount : int):
    author = ctx.message.author
    if author not in current_totals:
        await ctx.send(f'I dont have you registered, you can register with $registerme.')
        return
    else:
        current_totals[author] += amount
        await ctx.send(f'I have added ${amount} to your account, you now have ${current_totals[author]}.')

bot.run(TOKEN)
