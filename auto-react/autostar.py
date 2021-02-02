import asyncio
import emoji

import discord
from discord.ext import commands

class Autoreact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.api.get_plugin_partition(self)

	@client.event
   async def on_message(message):
     if(message.channel.id == "775039612053094420"):
     await client.add_reaction(message, "⭐")
		
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
