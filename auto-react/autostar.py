import asyncio
import discord
from discord.ext

class Autoreact(commands.Cog):
     def __init__(self, bot):
        self.bot = bot
 
@commands.Cog.listener()
async def on_message(message):
    if(message.channel.id == "775039612053094420"):
        await client.add_reaction(message, "⭐")
		
		
def setup(bot):
    bot.add_cog()
