from func import *  
from discord.ext import commands  
import discord 
import os
import asyncio

# Configurando os intents e a instância do bot
intents = discord.Intents.default()  
intents.message_content = True

# .env
idPayment = 1331368645149855754
idReaction = 1332328985794707550
idRole = 1331603876368875530
discordKey = os.getenv("DISCORD-KEY")

# Inicializa o bot com o prefixo '!' e os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)  

# Função que é chamada quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')  
    print(f'Uptime: {round(bot.latency * 1000)}ms')

    # Limpeza e mensagens no Reaction Chat
    asyncio.create_task(deleteChat(id=idReaction, bot=bot))
    asyncio.create_task(reactPutz(idChannel=idReaction,idRole=idRole,bot=bot))
    
    # Limpeza e mensagens no Payment Chat
    asyncio.create_task(deleteChat(id=idPayment, bot=bot))
    asyncio.create_task(paymentMessage(id=idPayment, bot=bot))


# Inicia o bot com o token fornecido
bot.run(discordKey)
