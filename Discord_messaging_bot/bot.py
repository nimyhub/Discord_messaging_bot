import json
import io
import random
import asyncio

# Load config.json
CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

config = load_config()

import discord
from discord.ext import commands

CHANNEL_ID = config.get("channel_id", 0)
USER_ID = config.get("user_id", 0)
TOKEN = config.get("token","none")
PREFIX = config.get("prefix","!")
COOLDOWN_SEC = config.get("cooldown_seconds",30)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Command is on cooldown. Try again in {int(error.retry_after)} seconds.")
    else:
        raise error

@bot.command(name='summon')
@commands.cooldown(rate=1, per=COOLDOWN_SEC, type=commands.BucketType.user)
async def summon(ctx, message: str):
    if CHANNEL_ID is None:
        await ctx.send("No target channel set. Update the config")
        return

    if USER_ID is None:
        await ctx.send(f"No user_id set. Update the config")
        return

    user = await bot.fetch_user(USER_ID)
    if user is None:
        await ctx.send("User not found or bot cannot access this user.")
        return
    
    await ctx.send(f"Summon in progress in {channel.mention}.")

    # Send DM
    if message is None:
        try:
            rand = random.randint(1, 1)
            if rand == 1:
                await user.send(f"GET YOUR ASS ON!")
            
            if rand == 2:
                await user.send(f"PETTER QUICK! HÅVARD IS GETTING NAKED ON CAM RIGHT NOW!")
            
            if rand == 3:
                await user.send(F"An incoming missile is headed straight for your entire Magic collection.  You have 5 minutes to respond in order to call of the strike. Text 'Im here' to {ctx.author}.")
        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")
    else:
        try:
            rand = random.randint(1, 2)
            if rand == 1:
                await user.send(f"{ctx.author} summons you with: {message}")
            
            if rand == 2:
                await user.send(f"Dear Sir Petter, On behalf off the great King/Queen {ctx.author} we request you listen carefully to the following message {message}")
        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")

    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        await ctx.send("Saved channel not found or bot lacks access.")
        return

    variant = random.randint(1, 5)

    if variant == 1:
        await channel.send(f"<@{USER_ID}> GET")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> YOUR")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> ASS")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> OVER")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> HERE")

    elif variant == 2:
        await channel.send(f"<@{USER_ID}> A TANK STUCK IN A SWAMP IS FASTER THAN YOU.")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> GET ON!")

    elif variant == 3:
        await channel.send(f"<@{USER_ID}>, You have one (1) new message from {ctx.author}. Display message?")
        await channel.send(f"||{message}||")
        await asyncio.sleep(5)
        await channel.send(f"<@{USER_ID}>, Would you like to reply?")

    elif variant == 4:
        await channel.send(f"<@{USER_ID}> YOU HAVE 2 SECONDS TO SHOW UP BEFORE HÅVARD STARTS FILMING A NEW VIDEO WITHOUT YOU")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> ONE!")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> TWO!")
        await asyncio.sleep(1)
        await channel.send(f"welp, too late ¯\_(ツ)_/¯")
    
    elif variant == 5:
        await channel.send(f"<@{USER_ID}> *jingle jingle*")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> **Magic the gathering**")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> *jingle jingle*")

bot.run(TOKEN)