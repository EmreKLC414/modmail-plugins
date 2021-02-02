import asyncio
import discord

@client.event
async def on_message(message):
    if(message.channel.id == "your_channel_id_here"):
        await client.add_reaction(message, "⭐")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
