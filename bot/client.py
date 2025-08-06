import discord
from discord.ext import commands
from bot.config import PREFIX
from bot.commands import register_commands

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

register_commands(bot)