import discord
from discord.ext import commands

class Autoreact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

@commands.Cog.listener()
async def on_message(self, message):
    if message.author.bot:
        return
    if int(message.channel.id) == 802867247772074004:
        await message.channel.send("Hello.")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
