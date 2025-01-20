import mercadopago

sdk = mercadopago.SDK("APP_USR-2733442010410611-012009-a605d25617a3512ac258afe7e6b62021-2224050184")

request = {
	"items": [
		{
			"id": "1234",
			"title": "Dummy Title",
			"description": "Dummy description",
			"picture_url": "https://www.myapp.com/myimage.jpg",
			"category_id": "car_electronics",
			"quantity": 1,
			"currency_id": "BRL",
			"unit_price": 10,
		},
	],
}

preference_response = sdk.preference().create(request)
preference = preference_response["response"]
print(preference['init_point'])
print(preference)