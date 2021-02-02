import asyncio
import discord

@commands.Autoreact.listener()
async def on_message(message):
    if(message.channel.id == "802867247772074004"):
        await client.add_reaction(message, "⭐")
	
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
