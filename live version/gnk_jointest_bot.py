import discord
import asyncio
from discord.ext import commands,tasks
from discord.utils import get

bot=commands.Bot(command_prefix='GnK')
token='NzQyMzc1OTUzNTA5OTA4NTcw.XzFNew.xb1Jw4IK5LJcquxjwIvmO5hJEok'
version='V1.0.0'

@bot.event
async def on_ready():
    print("bot login test")
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(version))

@bot.event
async def on_member_join(member):
    guild=bot.get_guild(742343312245129297)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True,send_messages=True),
    }
    await guild.create_text_channel(str(member.name),overwrites=overwrites)


bot.run(token)