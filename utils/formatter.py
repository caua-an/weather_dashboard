
def show_daily_forecast(daily_data):
    # iteração com o numero de dias
    for item in range(len(daily_data['time'])):
        print(daily_data["time"][item])
        print(f"Max: {daily_data["temperature_2m_max"][item]}°C")
        print(f"Min: {daily_data["temperature_2m_min"][item]}°C")
        print(f"Chuva: {daily_data["precipitation_sum"][item]}mm\n")