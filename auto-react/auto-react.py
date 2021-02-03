import discord
import emoji
from discord.ext import commands

class Autoreact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

@commands.Cog.listener()
async def on_message(self, ctx):
    if(message.self.bot.get_channel(802867247772074004)):
        await ctx.add_reaction(self "⭐")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
