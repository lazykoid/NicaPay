import mercadopago
import os

mercadoPagoKey = discord_token = os.getenv("MERCADO-KEY")
# Inicializando o SDK do Mercado Pago com a chave de aplicativo
sdk = mercadopago.SDK(mercadoPagoKey)
# Definindo os itens disponíveis para compra num dicionario-lista.
requests = {
    "items": [
        {
            "id": "1",
            "title": "Servidor 4Gb - Padrão",
            "description": "Servidor Minecraft 4Gb - Padrão",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2f/Dirt.png/revision/latest?cb=20220112085643",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 29.9,
        },
        {
            "id": "2",
            "title": "Servidor 6Gb - Padrão",
            "description": "Servidor Minecraft 6Gb - Padrão",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c1/Oak_Planks.png/revision/latest/scale-to-width-down/250?cb=20220112085657",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 39.9,
        },
        {
            "id": "3",
            "title": "Servidor 8Gb - Avançado",
            "description": "Servidor Minecraft 8Gb - Avançado",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/7/72/Block_of_Gold_JE6_BE3.png/revision/latest?cb=20200226013525",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 49.9,
        },
        {
            "id": "4",
            "title": "Servidor 12Gb - Extremo",
            "description": "Servidor Minecraft 12Gb - Extremo",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c8/Block_of_Diamond_JE5_BE3.png/revision/latest?cb=20200226013851",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 69.9,
        },
        {
            "id": "5",
            "title": "Servidor 16Gb - Extremo",
            "description": "Servidor Minecraft 16Gb - Extremo",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/31/Block_of_Netherite_JE1_BE1.png/revision/latest?cb=20200320021504",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 89.9,
        },
    ]
}
# Função para criar um pagamento baseado no ID do item
def createPayment(id: int):
    match id:
        case 1:
            return {"items": [requests["items"][0]]}  # Retorna o dicionário do servidor 4Gb/Padrão
        case 2:
            return {"items": [requests["items"][1]]}  # Retorna o dicionário do servidor 6Gb/Padrão
        case 3:
            return {"items": [requests["items"][2]]}  # Retorna o dicionário do servidor 8Gb/Avançado
        case 4:
            return {"items": [requests["items"][3]]}  # Retorna o dicionário do servidor 12Gb/Extremo
        case 5:
            return {"items": [requests["items"][4]]}  # Retorna o dicionário do servidor 16Gb/Extremo
        case _:
            return None  # Caso não encontre nenhum item correspondente

# Função para fazer uma requisição de pagamento com os dados do pedido
def makeRequest(order:dict):
    preference_response = sdk.preference().create(order)
    preference = preference_response["response"]
    return preference['init_point']