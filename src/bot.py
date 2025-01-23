from func import *  
from discord.ext import commands  
import discord 
import os

# Configurando os intents e a instância do bot
intents = discord.Intents.default()  
intents.message_content = True

# .env
idPayment = 1331368645149855754
idReaction = 1331977885367537724
discordKey = os.getenv("DISCORD-KEY")

# Inicializa o bot com o prefixo '!' e os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)  

# Função que é chamada quando o bot está pronto
@bot.event
async def on_ready():    
    print(f'Logged on as {bot.user}!')  
    print(f'Uptime: {round(bot.latency * 1000)}ms')
    # Payment Chat
    await deleteChat(id=idPayment, bot=bot)  
    await paymentMessage(id=idPayment, bot=bot)  

    # Reaction Chat
    # await deleteChat(id=idReaction, bot=bot) 
    # await reactPutz(id=idReaction,bot=bot)

# Inicia o bot com o token fornecido
bot.run(discordKey)
