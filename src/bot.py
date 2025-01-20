from func import *
from discord.ext import commands
import discord
    
# Set up intents and bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    id = 1330954025767800954
    print(f'Logged on as {bot.user}!')
    await deleteChat(bot=bot,id=id)
    await send_embedded_message(id,bot=bot)

# Run the bot
bot.run('MTMzMDg5NjI5NzIwNDUxOTAzMw.Gkcsev.H0wzJsvQsDCgOwHqPC1buu0mudoXq0r2DJdbxs')
