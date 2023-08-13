import requests 
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '805b45e75443241d198cf4e829930bdc'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1900 })
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1900 })
    assert response.json()['trainer_name'] == 'Rostek'

@pytest.mark.parametrize('key, value', [('name', 'Little'), 
                                        ('trainer_id', '1900'),
                                         ('attack', '1.0')])

def test_parts_of_answer(key,value):
    response = requests.get(f'{host}/pokemons', params = {'trainer_id' : 1900})
    assert response.json()[0][key] == value