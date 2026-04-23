import requests

url_api = "https://api.open-meteo.com/v1/forecast"

def get_daily_forecast(latitude, longitude):
    # parametros definidos para requisição de acordo com latitude e longitude
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current-weather": True,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum"

    }
    # recebe o endpoint da url
    try:
        response = requests.get(url_api, params=params, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    # transforma em um formato json
    data = response.json()


    # retorna as informaçoes sobre o clima dos proximos 7 dias
    return data['daily']
