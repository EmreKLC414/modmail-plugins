import asyncio
from discord.ext

class Autoreact(commands.Cog):

	@client.event
	async def on_message(message):
 		if(message.channel.id == "775039612053094420"):
		await client.add_reaction(message, "⭐")
		
		
def setup(bot):
    bot.add_cog(Autoreact(bot))
