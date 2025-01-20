from discord.ext import commands
import discord
# Set up intents and bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    #print(f'Avg Ping {bot.Ping}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description="This is a response to the $ping command.",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

# Run the bot
bot.run('MTMzMDg5NjI5NzIwNDUxOTAzMw.Gkcsev.H0wzJsvQsDCgOwHqPC1buu0mudoXq0r2DJdbxs')
