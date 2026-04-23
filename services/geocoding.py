import requests

# ending da API para pesquisar lat,log de uma cidade
url_api = "https://geocoding-api.open-meteo.com/v1/search"

def geocode(city_name):

    # parametro essencial é o nome da cidade
    params = {
        "name": city_name
    }
    # tenta fazer o request da url
    try:
        response = requests.get(url_api, params=params, timeout=10)
    except requests.RequestException:
        return None
    if response.status_code != 200:
        return None

    data = response.json()

    # caso não exista resultados sobre essa cidade
    if "results" not in data:
        return None

    # geocode retorna uma tupla de latitude e longitude
    return data['results'][0]['latitude'], data['results'][0]['longitude']
