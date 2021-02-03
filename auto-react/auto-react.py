import discord
from discord.ext import commands

class Autoreact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

@commands.Cog.listener()
async def on_message(self, message):
    if message.author.bot:
        return
    if message.channel.id == 773689755556380703:
        await message.channel.send("Hello.")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
