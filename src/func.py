from discord.ext import commands
import discord
import payment

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

            **Suporte Especializado será acrescentado mais R$ 9,90!
            Para saber mais sobre o Suporte Especializado clique no 👻
            ** 
        """,
        color=discord.Color.from_str("#6eaf5e"),
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
    await message.add_reaction('❔')

    reaction, user = await bot.wait_for('reaction_add', check=checkUserReaction)

    if reaction.emoji == '❤️':
        await channel.send('Você selecionou o Plano 4Gb!')
        await channel.send('Após o pagamento, enviar comprovante para @koidfas!')
    elif reaction.emoji == '🤎':
        await channel.send('Você selecionou o Plano 6Gb!')
        await channel.send('Após o pagamento, enviar comprovante para @koidfas!')
    elif reaction.emoji == '💚':
        await channel.send('Você selecionou o Plano 8Gb!')
        await channel.send('Após o pagamento, enviar comprovante para @koidfas!')
    elif reaction.emoji == '💛':
        await channel.send('Você selecionou o Plano 12Gb!')
        await channel.send('Após o pagamento, enviar comprovante para @koidfas!')
    elif reaction.emoji == '💜':
        await channel.send('Você selecionou o Plano 16Gb!')
        await channel.send('Após o pagamento, enviar comprovante para @koidfas!')
    elif reaction.emoji == '❔':
        await user.send("""
        # Suporte Especializado

        Nosso **Suporte Especializado** foi criado para oferecer uma **experiência completa e personalizada** para os jogadores de Minecraft que desejam **otimizar seus servidores e modpacks**. 
        Com uma taxa adicional de apenas **R$ 9,90**, você terá acesso a uma série de serviços que garantem que seu servidor esteja sempre funcionando da melhor forma possível. Veja o que está incluído:

            1. Configuração de Servidores: Nossa equipe especializada irá **configurar seu servidor Minecraft** de acordo com suas necessidades, garantindo que tudo esteja pronto para você e seus amigos jogarem sem complicações.

            2. Configuração de Modpacks: Se você deseja jogar com **modpacks personalizados**, cuidaremos de toda a configuração necessária, garantindo que todos os mods funcionem perfeitamente juntos.

            3. Criação de Modpacks: Se você tem uma ideia específica em mente, podemos ajudar a **criar um modpack personalizado** que atenda às suas expectativas e ao estilo de jogo desejado.

            4. Manutenção do Servidor: Mantemos seu servidor **atualizado e funcionando sem problemas.** Isso inclui atualizações regulares, monitoramento de desempenho e resolução de quaisquer problemas que possam surgir.

            5. Atendimento Prioritário: Com o **Suporte Especializado**, você terá acesso a **atendimento prioritário**. Isso significa que suas solicitações e dúvidas serão tratadas com urgência, garantindo que você obtenha respostas e soluções mais rapidamente.

        Aproveite essa oportunidade para ter um servidor Minecraft **configurado e mantido por profissionais**, permitindo que você se concentre apenas em se divertir!          
            """)
        await channel.send('Enviamos uma mensagem no seu privado!')


async def deleteChat(id:int,bot):
    tmp = bot.get_channel(1330954025767800954)
    async for message in tmp.history(limit=1):
        if message:
            await tmp.purge(limit=None)
            break
        