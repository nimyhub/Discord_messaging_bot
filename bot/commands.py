import discord
from discord.ext import commands
from bot.config import USER_ID, CHANNEL_ID, COOLDOWN_SEC, PREFIX, SMS_CALL
from bot.messaging import send_message, get_sms_message
from bot.sms import send_sms, set_phone_number

def register_commands(bot):
    @bot.command(name='setphone')
    async def set_phone(ctx, new_phone_number: str = None):
        if ctx.author.id != USER_ID:
            await ctx.send("You are not authorized to set the phone number.")
            return
        if not SMS_CALL:
            await ctx.send("SMS/Calling feature is disabled in the config.")
            return
        if new_phone_number is None:
            await ctx.send(f"Please provide a phone number. Usage: {PREFIX}setphone <number>")
            return

        set_phone_number(new_phone_number)
        await ctx.send("Phone number set successfully (stored only temporarily).")

    @bot.command(name='summon')
    @commands.cooldown(rate=1, per=COOLDOWN_SEC, type=commands.BucketType.user)
    async def summon(ctx, *, message: str = None):
        user = await bot.fetch_user(USER_ID)
        channel = bot.get_channel(CHANNEL_ID)

        if not user or not channel:
            await ctx.send("User or channel not found.")
            return

        await ctx.send(f"Summon in progress in {channel.mention}.")

        try:
            if message is None:
                await send_message("dm_no_messages", user, {"author": ctx.author.name})
            else:
                await send_message("dm_messages", user, {"author": ctx.author.name, "message": message})
        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")

        await send_message("server_pings", channel, {
            "author": ctx.author.name,
            "message": message or "GET ON",
            "user_id": str(user.id)
        })

    @bot.command(name='important_summon')
    @commands.cooldown(rate=1, per=COOLDOWN_SEC*60, type=commands.BucketType.user)
    async def important_summon(ctx, *, message: str = None):
        await summon(ctx, message=message)
        sms_text = await get_sms_message("sms_messages", {"author": ctx.author.name, "message": message})
        if sms_text:
            await send_sms(sms_text)
