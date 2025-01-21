import mercadopago
sdk = mercadopago.SDK("APP_USR-2733442010410611-012009-a605d25617a3512ac258afe7e6b62021-2224050184")
# Supondo que você já tenha a variável requests definida conforme anteriormente
requests = {
    "items": [
        {
            "id": "1",
            "title": "Servidor 4Gb/Padrão",
            "description": "Servidor Minecraft 4Gb/Padrão",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2f/Dirt.png/revision/latest?cb=20220112085643",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 29.9,
        },
        {
            "id": "2",
            "title": "Servidor 6Gb/Padrão",
            "description": "Servidor Minecraft 6Gb/Padrão",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2f/Dirt.png/revision/latest?cb=20220112085643",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 39.9,
        },
        {
            "id": "3",
            "title": "Servidor 8Gb/Avançado",
            "description": "Servidor Minecraft 8Gb/Avançado",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2f/Dirt.png/revision/latest?cb=20220112085643",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 49.9,
        },
        {
            "id": "4",
            "title": "Servidor 12Gb/Extremo",
            "description": "Servidor Minecraft 12Gb/Extremo",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2f/Dirt.png/revision/latest?cb=20220112085643",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 69.9,
        },
        {
            "id": "5",
            "title": "Servidor 16Gb/Extremo",
            "description": "Servidor Minecraft 16Gb/Extremo",
            "picture_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2f/Dirt.png/revision/latest?cb=20220112085643",
            "category_id": "server",
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": 89.9,
        },
    ]
}

def createPayment(id: int):
    # Encontrar o item correspondente com o id
    item = next((item for item in requests["items"] if int(item["id"]) == id), None)
    
    match item:
        case None:
            return None  # Retorna None se o item não for encontrado
        case {'id': id, 'title': title, 'description': description, 'unit_price': unit_price}:
            return {
                "id": id,
                "title": title,
                "description": description,
                "unit_price": unit_price
            }

# Testando a função
result = createPayment(2)
if result:
    print(result)  # Aqui você pode usar os dados retornados como quiser
else:
    print("Item não encontrado.")

# Você pode usar o resultado em outra função
def processPayment(payment_info):
    if payment_info:
        # Lógica para processar o pagamento
        print(f"Processando pagamento para: {payment_info['title']} no valor de {payment_info['unit_price']} BRL")
    else:
        print("Nenhum pagamento para processar.")

# Testando a função de processamento com o resultado
processPayment(result)
