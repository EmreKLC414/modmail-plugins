import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class Publish(commands.Cog): 
    """Publish messages sent in announcement channels"""
    
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def publish(self, message_id: discord.TextChannel):
        if message.channel.id == 802867247772074004:
            await message.publish()
            
                                        
def setup(bot):
    bot.add_cog(Publish(bot))

 

# Examples for multiple usage
#
#   
# For Multiple Channel;
#         if message.channel.id in [channel_id_one, channel_id_two, channel_id_three]:
#            await message.add_reaction("emojihere")
#
#
#For Multiple Emoji
#        if message.channel.id == Channel_ID:
#            await message.add_reaction("emojihere")
#            await message.add_reaction("emojihere")
