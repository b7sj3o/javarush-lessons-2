# import json
# import requests
#
#
# api_key = 'ВАШ_КЛЮЧ_OPENWEATHERMAP'
# city="Lviv"
# url = f"http://api.openweathermap.org/data/2.5/weather"
#
# def get_weather(city: str) -> dict:
#     params = {"q": city, "appid": api_key, "units": "metric"}
#     response = requests.get(url, params=params, timeout=10)
#
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "city": data["name"],
#             "weather_description": data["weather"][0]["description"],
#             "temperature": data["main"]["temp"],
#             "wind_speed": data["wind"]["speed"],
#         }
#     elif response.status_code == 404:
#         print(f"Міста '{city}' не знайдено")
#     elif response.status_code == 429:
#         print("Ви зробили забагато запитів! Зачекайте")
#     else:
#         print(response.status_code, response.reason)
#         print(response.json())
#
#     return {}
#
#
# def main():
#     while True:
#         city = input(">>> ")
#
#         if city == "":
#             break
#
#         weather = get_weather(city)
#
#         if weather:
#             print((
#                 f"Місто: {weather["city"]}\n"
#                 f"Температура: {weather['temperature']}\n"
#                 f"Швидкість вітру: {weather['wind_speed']}\n"
#                 f"Опис погоди: {weather['weather_description']}\n"
#             ))
#
#
# if __name__ == "__main__":
#     main()


import requests

r = requests.get(
    'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange',
    params={'json': ''}, timeout=10
)
rates = {c['cc']: c['rate'] for c in r.json()}
print(f"USD: {rates['USD']}  EUR: {rates['EUR']}  PLN: {rates['PLN']}")

# r = requests.get('https://api.frankfurter.dev/v2/rates',
#                  params={'base': 'EUR', 'quotes': 'USD,PLN'}, timeout=10)
# print(r.json())