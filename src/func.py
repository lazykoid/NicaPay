from discord.ext import commands
import discord
import payment

# Preços de Planos
# 4Gb 29,9 Recomendado para SMP/Survival Vanilla Pequenos.
# 6Gb 39,9 Recomendado para Modpacks Médios e até 6 players
# 8Gb 49,9 Recomendado para Modpacks Médios/Grandes e até 8 players
# 12Gb 69,9 Recomendado para Modpacks Grandes e até 12+ players
# 16Gb 89,9 Recomendado para Modpacks Grandes e até 16+ players
# Support++ mais 10,00

async def paymentMessage(id:int,bot):
    def checkUserReaction(reaction, user):
        return user != bot.user and reaction.message == message
    
    # Get the channel object
    channel = bot.get_channel(id)
    
    # Create an embedded message
    embed = discord.Embed(
        title="Planos de Servidores!",
        type="rich",
        description="""
            ## 4Gb RAM e Processamento Padrão - R$ 29,90
            ### Recomendado para SMP/Survival Vanilla Pequenos.
            Clique no ❤️ para selecionar-lo!
            ## 6Gb RAM e Processamento Padrão - R$ 39,90
            ### Recomendado para Modpacks Médios e até 6 players
            Clique no 🤎 para selecionar-lo!
            ## 8Gb RAM e Processamento Avançado - R$ 49,90 
            ### Recomendado para Modpacks Médios/Grandes e até 8 players
            Clique no 💚 para selecionar-lo!
            ## 12Gb RAM e Processamento Extremo - R$ 69,90
            ### Recomendado para Modpacks Grandes e até 12+ players
            Clique no 💛 para selecionar-lo!
            ## 16Gb RAM e Processamento Extremo - R$ 89,90
            ### Recomendado para Modpacks Grandes e até 16+ players
            Clique no 💜 para selecionar-lo!

            **Suporte Especializado será acrescentado mais R$ 10,00!
            Para saber mais sobre o Suporte Especializado clique no 👻
            ** 
        """,
        color=discord.Color.green(),
        timestamp=discord.utils.utcnow()
    )

    embed.set_footer(
        text="@koidfas"
    )
    # Send the embedded message to the channel
    message = await channel.send(embed=embed)
    
    # Add reactions as buttons
    await message.add_reaction('❤️')  
    await message.add_reaction('🤎')  
    await message.add_reaction('💚')
    await message.add_reaction('💛')
    await message.add_reaction('💜')
    await message.add_reaction('👻')

    reaction, user = await bot.wait_for('reaction_add', check=checkUserReaction)

    # Handle user reaction
    if reaction.emoji == '❤️':
        await channel.send('Você selecionou o Plano 4Gb!')
    elif reaction.emoji == '🤎':
        await channel.send('Você selecionou o Plano 6Gb!')
    elif reaction.emoji == '💚':
        await channel.send('Você selecionou o Plano 8Gb!')
    elif reaction.emoji == '💛':
        await channel.send('Você selecionou o Plano 12Gb!')
    elif reaction.emoji == '💜':
        await channel.send('Você selecionou o Plano 16Gb!')
    elif reaction.emoji == '👻':
        await channel.send('Enviamos uma mensagem no seu privado!')


async def deleteChat(id:int,bot):
    tmp = bot.get_channel(1330954025767800954)
    async for message in tmp.history(limit=1):
        if message:
            await tmp.purge(limit=None)
            break
