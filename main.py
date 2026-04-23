from services import weather_api, geocoding
from utils import formatter

# inserir nome da cidade
cidade = input('Digite o nome da cidade: ')
# transforma em tupla de latitude e longitude
cidade = geocoding.geocode(cidade)

# situação em que o geocode() retornou None
if cidade is None:
    print('Nao foi possivel localizar a cidade informada.')
    raise SystemExit(1)

daily_data = weather_api.get_daily_forecast(cidade[0], cidade[1])

# situação em que get_daily_forecast retornou None
if daily_data is None:
    print('Nao foi possivel consultar a previsao do tempo.')
    raise SystemExit(1)

formatter.show_daily_forecast(daily_data)

