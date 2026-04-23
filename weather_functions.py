import requests
import time

url_api = "https://api.open-meteo.com/v1/forecast"

# parametros definidos para requisição de Campina Grande
params = {
    "latitude": -7.23,
    "longitude": -35.88,
    "current-weather": True,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum"

}

# recebe o endpoint da url
response = requests.get(url_api, params=params)
# transforma em um formato json
data = response.json()

# iteração com o numero de dias
for item in range(len(data["daily"]['time'])):
    print(data["daily"]["time"][item])
    print(f"Max: {data["daily"]["temperature_2m_max"][item]}°C")
    print(f"Min: {data["daily"]["temperature_2m_min"][item]}°C\n")
