import discord
from discord.ext import commands

class Autoreact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

@commands.command
async def on_message(self, ctx, message):
    if(message.channel.id == "802867247772074004"):
        await ctx.add_reaction(message, "⭐")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
