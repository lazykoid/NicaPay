from discord.ext import commands
import discord

async def send_embedded_message(channel_id,bot):
    # Get the channel object
    channel = bot.get_channel(channel_id)
    
    # Create an embedded message
    embed = discord.Embed(
        title="Planos de Servidores!",
        type="rich",
        description="Clique na reação correspondente ao Plano.",
        color=discord.Color.blue()
    )
    embed.add_field(    
        name="# testing",
        value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )

    # Send the embedded message to the channel
    await channel.send(embed=embed)

async def deleteChat(id:int,bot):
    tmp = bot.get_channel(1330954025767800954)
    async for message in tmp.history(limit=1):
        if message:
            await tmp.purge(limit=None)
            break
