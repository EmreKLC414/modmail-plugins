import discord
from discord.ext import commands

class Autoreact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

@commands.command
async def on_message(self, message):
    if(message.bot.get_channel(802867247772074004)):
        await ctx.message.add_reaction("\u2b50")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
