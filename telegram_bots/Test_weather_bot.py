import telebot
import tokens
from pyowm import OWM

bot = telebot.TeleBot(tokens.test3456_weather_bot_token)
owm = OWM(tokens.OWM_key)
mgr = owm.weather_manager()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, введи название города.')


@bot.message_handler(content_types=['text'])
def send_text(message):
    city = mgr.weather_at_place(message.text)
    city_weather_temperature = city.weather.temperature(
        'celsius')['temp']
    city_weather_wind = city.weather.wind()
    city_weather_humidity = city.weather.humidity
    bot.send_message(message.chat.id,
                     f'Температура: {city_weather_temperature} градусов\n'
                     f"Скорость ветра: {city_weather_wind['speed']} метров в секунду\n"
                     f"Влажность: {city_weather_humidity}%")


bot.polling()
