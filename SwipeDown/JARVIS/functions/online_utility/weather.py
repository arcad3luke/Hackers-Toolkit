import json
import requests
from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu

def get_weather_report(city):
    OPENWEATHER_APP_ID = 'REDACTED'
    session = requests.session()
    session.verify = True
    # Fahrenheit
    res_f = session.post(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=imperial").json()
    weather_f = res_f["weather"][0]["main"]
    temperature_f = res_f["main"]["temp"]
    feels_like_f = res_f["main"]["feels_like"]
    # Celcius
    res_c = session.post(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather_c = res_c["weather"][0]["main"]
    temperature_c = res_c["main"]["temp"]
    feels_like_c = res_c["main"]["feels_like"]
    json.dumps(f'{weather_f}, {temperature_f}°F, {feels_like_f}°F\n {weather_c}, {temperature_c}°C, {feels_like_c}°C')

def main():
    show_menu = ConsoleMenu(title='Get the weather!', clear_screen=True, show_exit_option=True, exit_option_text='[+] Quit')
    weather = FunctionItem('[+] Get the weather', get_weather_report(city=input('What city?')))
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(weather)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()