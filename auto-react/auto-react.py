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
        if message.channel.id == 775039612053094420: #Channel_ID
            await message.add_reaction("\u2b50")  # Emoji
        if message.channel.id == 814142601145221160:
            await message.add_reaction("<:iyi:809187585913126912>")
            await message.add_reaction("<:gg:809187585779433496>")
    
        
def setup(bot):
    bot.add_cog(Autoreact(bot))

 

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
