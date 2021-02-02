import asyncio
import emoji
from core import checks
import discord
from discord.ext import commands


   @client.event
   async def on_message(message):
     if(message.channel.id == "775039612053094420"):
     await client.add_reaction(message, "⭐")
		
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
