from func import *  
from discord.ext import commands  
import discord 

# Configurando os intents e a instância do bot
intents = discord.Intents.default()  
intents.message_content = True

# Inicializa o bot com o prefixo '!' e os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)  

# Função que é chamada quando o bot está pronto
@bot.event
async def on_ready():  
    id = 1330954025767800954  # ID do canal onde as mensagens de pagamento serão enviadas
    print(f'Logged on as {bot.user}!')  
    print(f'Uptime: {round(bot.latency * 1000)}ms') 
    await deleteChat(id=id, bot=bot)  
    await paymentMessage(id, bot=bot)  

# Inicia o bot com o token fornecido
bot.run('MTMzMDg5NjI5NzIwNDUxOTAzMw.Gkcsev.H0wzJsvQsDCgOwHqPC1buu0mudoXq0r2DJdbxs')
