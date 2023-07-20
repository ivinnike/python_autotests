
import requests
import pytest

PROD_URL = 'https://api.pokemonbattle.me:9104'

# приходит с кодом 200
def test_status_code():
    response = requests.get(f'{PROD_URL}/trainers', params={'trainer_id': 1702})
    assert response.status_code == 200


# приходит строчка с именем моего тренера
def test_name():
    response = requests.get(f'{PROD_URL}/trainers', params={'trainer_id': 1702})
    assert response.json()['trainer_name'] == 'Space_x'