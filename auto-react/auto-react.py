import discord
from discord.ext import commands

class Autoreact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if not isinstance(message.channel, discord.TextChannel):
            return
        if message.channel.id == 802867247772074004: #ChannelID
            await message.add_reaction("\u2b50")
    
        
def setup(bot):
    bot.add_cog(Autoreact(bot))
