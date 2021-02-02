import asyncio
import discord
from discord.ext import commands

class Autoreact(commands.Cog):
    """
    test
    """
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

@bot.listen()
async def on_message(message):
    if(message.channel.id == "802867247772074004"):
        await client.add_reaction(message, "⭐")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
