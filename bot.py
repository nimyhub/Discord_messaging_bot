import json
import io
import random
import asyncio
import discord
from discord.ext import commands

# Load config.json
CONFIG_FILE = "config.json"
MESSAGE_FILE = "messages.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)
    
def load_messages():
    with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()
message_templates = load_messages()

CHANNEL_ID = config.get("channel_id", 0)
USER_ID = config.get("user_id", 0)
TOKEN = config.get("token","none")
PREFIX = config.get("prefix","!")
COOLDOWN_SEC = config.get("cooldown_seconds",30)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

async def send_message_sequence(category: str, reciver, context_vars: dict):
    versions = message_templates.get(category, {})
    if not versions:
        print(f"No templates found for category: {category}")
        return

    if isinstance(versions, dict):
        version_key = str(random.randint(1, len(versions)))
        sequence = versions.get(version_key, [])
        for step in sequence:
            text = step["text"].format(**context_vars)
            await reciver.send(text)
            await asyncio.sleep(step.get("delay", 0))

    elif isinstance(versions, list):
        chosen_text = random.choice(versions).format(**context_vars)
        await reciver.send(chosen_text)

    else:
        print(f"Unexpected template format for category: {category}")

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
async def summon(ctx, *,message: str = None):
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
    
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        await ctx.send("Saved channel not found or bot lacks access.")
        return
    
    await ctx.send(f"Summon in progress in {channel.mention}.")

    if message is None:
        try:
            await send_message_sequence("dm_no_messages", user, {"author": ctx.author.name})

        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")
    else:
        try:
            await send_message_sequence("dm_messages", user, {"author": ctx.author.name,"message": message})

        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")

    message = "GET ON"
    await send_message_sequence("server_pings", channel, {"author": ctx.author.name,"message": message, "user_id": str(user.id)})


bot.run(TOKEN)