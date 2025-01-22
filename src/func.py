from discord.ext import commands
import discord
import payment

# Função para enviar uma mensagem de pagamento
async def paymentMessage(id:int,bot):
    def checkUserReaction(reaction, user):
        return user != bot.user and reaction.message == message
    
    channel = bot.get_channel(id)
    
    # Cria uma mensagem incorporada (embed) com informações sobre os planos de servidores
    embed = discord.Embed(
        title="Planos de Servidores!",
        type="rich",
        description="## 4Gb RAM e Processamento Padrão - R$ 29,90\n### Recomendado para SMP/Survival Vanilla Pequenos.\nClique no ❤️ para selecionar-lo!\n## 6Gb RAM e Processamento Padrão - R$ 39,90\n### Recomendado para Modpacks Médios e até 6 players\nClique no 🤎 para selecionar-lo!\n## 8Gb RAM e Processamento Avançado - R$ 49,90 \n### Recomendado para Modpacks Médios/Grandes e até 8 players\n Clique no 💚 para selecionar-lo!\n## 12Gb RAM e Processamento Extremo - R$ 69,90\n### Recomendado para Modpacks Grandes e até 12+ players\n Clique no 💛 para selecionar-lo!\n## 16Gb RAM e Processamento Extremo - R$ 89,90\n### Recomendado para Modpacks Grandes e até 16+ players\nClique no 💜 para selecionar-lo!\n\n**Suporte Especializado será acrescentado mais R$ 9,90!\nPara saber mais sobre o Suporte Especializado clique no ❔** ",
        color=discord.Color.from_str("#6eaf5e"),
        timestamp=discord.utils.utcnow()
    )

    embed.set_footer(
        text="@koidfas"
    )
    
    message = await channel.send(embed=embed)
    
    # Adiciona Reacoes
    await message.add_reaction('❤️')  
    await message.add_reaction('🤎')  
    await message.add_reaction('💚')
    await message.add_reaction('💛')
    await message.add_reaction('💜')
    await message.add_reaction('❔')
    
    
    await channel.send('Após o pagamento, enviar comprovante para <@765732852054491167>!')

    user_reactions = {}
    while True:
        reaction, user = await bot.wait_for('reaction_add', check=checkUserReaction)

        # Checa se os usuarios já reagiram 3 vezes
        if user.id in user_reactions and sum(user_reactions[user.id].values()) >= 3:
            await user.send("Você já reagiu 3 vezes, Tente novamente mais tarde!")
            continue

        # Incrementa o counter para cada usuario
        if user.id not in user_reactions:
            user_reactions[user.id] = {}
        if reaction.emoji not in user_reactions[user.id]:
            user_reactions[user.id][reaction.emoji] = user_reactions[user.id].get(reaction.emoji, 0) + 1

        if reaction.emoji == '❤️':
            await user.send('Você selecionou o Plano 4Gb!')
            order = payment.createPayment(1)
            await user.send(payment.makeRequest(order))
        elif reaction.emoji == '🤎':
            await user.send('Você selecionou o Plano 6Gb!')
            order = payment.createPayment(2)
            await user.send(payment.makeRequest(order))
        elif reaction.emoji == '💚':
            await user.send('Você selecionou o Plano 8Gb!')
            order = payment.createPayment(3)
            await user.send(payment.makeRequest(order))
        elif reaction.emoji == '💛':
            await user.send('Você selecionou o Plano 12Gb!')
            order = payment.createPayment(4)
            await user.send(payment.makeRequest(order))
        elif reaction.emoji == '💜':
            await user.send('Você selecionou o Plano 16Gb!')
            order = payment.createPayment(5)
            await user.send(payment.makeRequest(order))
        elif reaction.emoji == '❔':
            embedDM= discord.Embed(
                title="Suporte Especializado",
                type="rich",
                description="Nosso **Suporte Especializado** foi criado para oferecer uma **experiência completa e personalizada** para os jogadores de Minecraft que desejam **otimizar seus servidores e modpacks**. \nCom uma taxa adicional de apenas **R$ 9,90**, você terá acesso a uma série de serviços que garantem que seu servidor esteja sempre funcionando da melhor forma possível. \n## **Veja o que está incluído:**\n### Configuração de Servidores: \nNossa equipe especializada irá **configurar seu servidor Minecraft** de acordo com suas necessidades, garantindo que tudo esteja pronto para você e seus amigos jogarem sem complicações.\n### Configuração de Modpacks: \nSe você deseja jogar com **modpacks personalizados**, cuidaremos de toda a configuração necessária, garantindo que todos os mods funcionem perfeitamente juntos.\n### Criação de Modpacks: \nSe você tem uma ideia específica em mente, podemos ajudar a **criar um modpack personalizado** que atenda às suas expectativas e ao estilo de jogo desejado.\n### Manutenção do Servidor: \nMantemos seu servidor **atualizado e funcionando sem problemas.** Isso inclui atualizações regulares, monitoramento de desempenho e resolução de quaisquer problemas que possam surgir.\n### Atendimento Prioritário: \nCom o **Suporte Especializado**, você terá acesso a **atendimento prioritário**. Isso significa que suas solicitações e dúvidas serão tratadas com urgência, garantindo que você obtenha respostas e soluções mais rapidamente.\nAproveite essa oportunidade para ter um servidor Minecraft **configurado e mantido por profissionais**, permitindo que você se concentre apenas em se divertir!",
                color=discord.Color.from_str("#6eaf5e"),
                timestamp=discord.utils.utcnow()
                )
            await user.send(embed=embedDM)

# Função para apagar mensagens antigas no canal
async def deleteChat(id:int,bot):
    tmp = bot.get_channel(id)
    async for message in tmp.history(limit=1):
        if message:
            await tmp.purge(limit=None)
            break
        