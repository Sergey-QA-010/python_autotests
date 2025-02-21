import requests 

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '048003f3701bcb0035c6de1c05aa2426'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Картошка",
    "photo_id": 96
}

body_change = {
    "pokemon_id": "240685",
    "name": "Слон",
    "photo_id": 96
}

body_catch = {
    "pokemon_id": "240685"
}


## response = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
## print(response.text)
## pokemon_id = response.json()['id']
## print(pokemon_id)

## response = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change)
## print(response.text)

response =  requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response.text)







