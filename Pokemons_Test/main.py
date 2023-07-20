
import requests

TOKEN = '8853a094a52c68197b1b9bf896b06826'
PROD_URL = 'https://api.pokemonbattle.me:9104'

# Создаем покемона
response_create = requests.post(f'{PROD_URL}/pokemons', headers={
    'trainer_token': TOKEN,
    'Content-Type': 'application/json'
}, json={
    "name": "Пудель",
    "photo": "https://dolnikov.ru/pokemons/albums/020.png"
})
json_response = response_create.json()
print("Create Pokemon Response Code:", response_create.status_code)
print("Create Pokemon Response:", json_response)

# Получаем pokemon_id из ответа на создание покемона
pokemon_id = json_response.get('id')
print("Newly created Pokemon ID:", pokemon_id) 

# Смена имени покемона
response_editing = requests.put(f'{PROD_URL}/pokemons', headers={
    'trainer_token': TOKEN,
    'Content-Type': 'application/json'
}, json={
    "id": pokemon_id,
    "pokemon_id": pokemon_id,
    "name": "ПитоннаяКрыса",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
json_response = response_editing.json()
print("Create Pokemon Response Code:", response_editing.status_code)
print("Create Pokemon Response:", json_response)


# Поймать покемона в покетбол 
response_pokeball = requests.post(f'{PROD_URL}/trainers/add_pokeball', headers={
    'trainer_token': TOKEN,
    'Content-Type': 'application/json'
}, json={
    "id": pokemon_id,
    "pokemon_id": pokemon_id 
})
json_response = response_pokeball.json()
print("Catch Pokemon Response Code:", response_pokeball.status_code)
print("Catch Pokemon Response:", json_response)





# #Убить покемона
# response_сreate = requests.post(f'{PROD_URL}/pokemons/kill', headers= {
#     'trainer_token' : TOKEN,
#     'Content-Type' : 'application/json'
#   },
#               json={
#       "pokemon_id": "4866"
# })
# print(response_сreate.text)