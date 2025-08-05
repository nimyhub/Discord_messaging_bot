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

    # Send DM and PING #
    # ==================================================================================== #
    if message is None:
        try:
            rand = random.randint(1, 5)
            if rand == 1:
                await user.send(f"GET YOUR ASS ON!")
            
            if rand == 2:
                await user.send(f"PETTER QUICK! HÅVARD IS GETTING NAKED ON CAM RIGHT NOW!")
            
            if rand == 3:
                await user.send(f"An incoming missile is headed straight for your entire Magic collection.  You have 5 minutes to respond in order to call of the strike. Text 'Im here' to {ctx.author}.")

            if rand == 4:
                await user.send(f"HÅVARD IS GOING TO FILE FOR DIVORCE IF YOU DONT COME OVER HERE RIGHT NOW!!!")

            if rand == 5:
                await user.send("Petter. Listen carefully. This is not a test. The IKEA meatballs are under siege.")

        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")
    else:
        try:
            rand = random.randint(1, 3)
            if rand == 1:
                await user.send(f"{ctx.author} summons you with: {message}")
            
            if rand == 2:
                await user.send(f"Dear Sir Petter, On behalf off the great King/Queen {ctx.author} we request you listen carefully to the following message: {message}")
            
            if rand == 3:
                await user.send(f"{ctx.author} has spoken. Their words echo across the server: {message}. Interpret and act accordingly.")
            
            if rand == 4:
                await user.send(f"{ctx.author} has spoken. Their words echo across the server: {message}. Interpret and act accordingly.")

            if rand == 5:
                await user.send(f"A classified message from {ctx.author} has just been decrypted: {message} — proceed with extreme overreaction.")

            if rand == 6:
                await user.send(f"{ctx.author} screamed into the void. The void screamed back: {message}")

            if rand == 7:
                await user.send(f":warning:[HIGH PRIORITY] Transmission from Commander {ctx.author}: {message}. All units, mobilize.")

            if rand == 8:
                await user.send(f"Petter, you’ve been drafted. Orders from {ctx.author}: {message}. Desertion is not an option.")

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

    elif variant == 6:
        await channel.send(f"<@{USER_ID}> Your presence is required.")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> Immediately.")
        await asyncio.sleep(2)
        await channel.send(f"<@{USER_ID}> This is not a request.")

    elif variant == 7:
        await channel.send(f"<@{USER_ID}> GET")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}> THE")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}> FUCK")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}> ONLINE")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}> ***RIGHT NOW***")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}>")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}>")
        await asyncio.sleep(0.6)
        await channel.send(f"<@{USER_ID}>")

    elif variant == 8:
        await channel.send(f"<@{USER_ID}> HÅVARD just updated his relationship status.")
        await asyncio.sleep(1.5)
        await channel.send(f"<@{USER_ID}> it's complicated.")
        await asyncio.sleep(2)
        await channel.send(f"you better log in before he goes 'complicated' with someone else.")

    elif variant == 9:
        await channel.send(f"<@{USER_ID}> we found an unopened *Alpha Black Lotus*.")
        await asyncio.sleep(2)
        await channel.send(f"<@{USER_ID}> it’s yours if you log on in the next 30 seconds.")
        await asyncio.sleep(3)
        await channel.send(f"...it’s gone now.")

    elif variant == 10:
        await channel.send(f"Initiating summoning ritual: [<@{USER_ID}>]")
        await asyncio.sleep(5)
        await channel.send(f"summoning <@{USER_ID}> ▰▰▱▱▱▱▱▱▱ 23%")
        await asyncio.sleep(5)
        await channel.send(f"ERROR")
        await asyncio.sleep(1)
        await channel.send(f"Summon failed. Host is ignoring all pings.")
        await asyncio.sleep(1)
        await channel.send(f"Retrying with Magic bait and HÅVARD nudity")

    elif variant == 11:
        await channel.send(f"<@{USER_ID}> HÅVARD IS TAKING HIS SHIRT OFF.")
        await asyncio.sleep(1)
        await channel.send(f"<@{USER_ID}> HE SAID HE'LL GO ALL THE WAY IF YOU JOIN VC.")
    
    elif variant == 12:
        await channel.send(f"<@{USER_ID}>")
        await asyncio.sleep(0.5)
        await channel.send("I AM LOSING MY MIND")
        await asyncio.sleep(0.5)
        await channel.send("WHY ARE YOU NEVER ONLINE")
        await asyncio.sleep(0.5)
        await channel.send("IT'S BEEN 84 YEARS")
        await asyncio.sleep(0.5)
        await channel.send("VC.")
        await channel.send("**NOW!!**")

    elif variant == 13:
        await channel.send(f"<@{USER_ID}> SYSTEM ERROR")
        await asyncio.sleep(1)
        await channel.send("FRIEND NOT FOUND ONLINE")
        await asyncio.sleep(1)
        await channel.send("ATTEMPTING NETWORK RESTART")
        await asyncio.sleep(1)
        await channel.send("....")
        await asyncio.sleep(2)
        await channel.send("FAILED. USER[<@{USER_ID}>] IS STILL USELESS.")

    elif variant == 14:
        await channel.send(f"<@{USER_ID}> ALERT: Beta Dual Land for sale for €10.00.")
        await asyncio.sleep(4)
        await channel.send("You missed it.")
        await asyncio.sleep(1.5)
        await channel.send("You miss everything.")
        await asyncio.sleep(1)
        await channel.send("Get on....")
    
    elif variant == 15:
        await channel.send(f"<@{USER_ID}> HÅVARD is crying")
        await asyncio.sleep(1.5)
        await channel.send("He waited for you.")
        await asyncio.sleep(1.5)
        await channel.send("You never came")
        await asyncio.sleep(1.5)
        await channel.send("<@{USER_ID}> You let him down")


bot.run(TOKEN)