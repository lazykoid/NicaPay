from discord.ext import commands
import discord
import payment

async def paymentMessage(id:int,bot):
    # Get the channel object
    channel = bot.get_channel(id)
    
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
    message = await channel.send(embed=embed)
    
    # Add reactions as buttons
    await message.add_reaction('👍')  # Plano 1
    await message.add_reaction('👎')  # Plano 2
    await message.add_reaction('🤝')  # Plano 3

    # Wait for user reaction
    def check(reaction, user):
        return user != bot.user and reaction.message == message

    reaction, user = await bot.wait_for('reaction_add', check=check)

    # Handle user reaction
    if reaction.emoji == '👍':
        await channel.send('Você selecionou o Plano 1!')
    elif reaction.emoji == '👎':
        await channel.send('Você selecionou o Plano 2!')
    elif reaction.emoji == '🤝':
        await channel.send('Você selecionou o Plano 3!')

async def deleteChat(id:int,bot):
    tmp = bot.get_channel(1330954025767800954)
    async for message in tmp.history(limit=1):
        if message:
            await tmp.purge(limit=None)
            break
