import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio

class EmojiSuggestor(commands.Cog):
  
 
@commands.Cog.listener()
async def on_message(message):
    if(message.channel.id == "775039612053094420"):
        await client.add_reaction(message, "⭐")
		
		
def setup(bot):
    bot.load_extension(auto-react)