import requests

token = '805b45e75443241d198cf4e829930bdc' # Токен для PROD
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов PROD

# Создаю тренера
'''response = requests.post('https://api.pokemonbattle.me:9104', json = {
    "trainer_token": token,
    "email": "antonaktaev@yandex.ru",
    "password": "Antonaktaev1"
}, headers = {'Content-Type' : 'application/json'})'''

# Активирую тренера через почту
'''response_activation = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
}, headers = {'Content-Type' : 'application/json'})

print(response_activation.text)'''

# Меняю имя тренера и город
'''response_change_trainer = requests.put(f'{host}/trainers', json = {
    "name": "Rostek",
    "city": "Istan"
}, headers = {'Content-Type' : 'application/json',
               'trainer_token': token})

print(response_change_trainer.text)'''

# Создаю покемона
'''response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Евдакия",
    "photo": "https://dolnikov.ru/pokemons/albums/423.png"
}, headers = {'Content-Type' : 'application/json',
               'trainer_token': token})

print(response_add_pokemon.text)'''

# Смена имени покемона и аватара
'''response_change_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5787",
    "name": "Little",
    "photo": "https://dolnikov.ru/pokemons/albums/233.png"
}, headers = {'Content-Type' : 'application/json',
               'trainer_token': token})

print(response_change_pokemon.text)'''

# Добавляю покемона в покебол
'''response_pokemon_in_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = { 
    "pokemon_id": "5787",
}, headers = {'Content-Type' : 'application/json',       
               'trainer_token': token})

print(response_pokemon_in_pokeball.text)'''


