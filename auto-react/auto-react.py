import asyncio
import discord
from discord.ext import commands

class Autoreact(commands.Cog):
    """Test 1 2 3"""

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        bot.loop.create_task(self.load_variables())

@cog.listen()
async def on_message(message):
    if(message.channel.id == "802867247772074004"):
        await client.add_reaction(message, "⭐")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
