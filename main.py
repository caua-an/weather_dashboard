from services import weather_api
from utils import formatter

# inserir coordenadas
daily_data = weather_api.get_daily_forecast(-7.53, -35.88)
formatter.show_daily_forecast(daily_data)


