from consolemenu import *
from consolemenu.items import *


# import pyttsx3
# import datetime
# import os
#
# engine = pyttsx3.init('sapi5')
# engine.setProperty('rate', 190)
# engine.setProperty('volume', 1.0)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices)
#
#
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# def greetUser():
#     time = datetime.datetime.now()
#     current_hour = time.hour
#     if 6 >= current_hour <= 12:
#         speak(f"Good Morning {os.getenv('USER')}! How may I be of assistance?")
#     elif 12 >= current_hour <= 16:
#         speak(f"Good Afternoon {os.getenv('USER')}! How may I be of assistance?")
#     elif 16 >= current_hour <= 19:
#         speak(f"Good Evening {os.getenv('USER')}! How may I be of assistance?")
#     elif 19 >= current_hour <= 6:
#         speak(f"Up late are we, {os.getenv('USER')}? How may I be of assistance?")
#     else:
#         speak('What\'s the time?')


def main():
    # greetUser()
    title = 'SwipeDown'
    subtitle = ('Welcome to SwipeDown! \n'
                'This repository is a collective of \n'
                'tools written by a community\n'
                'of like-minded individuals who want \n'
                'to help other programmers and\n'
                'entry-level pentesters get a little\n'
                '\'head start\' into the world\n'
                'of cybersecurity. This project is a\n'
                'result of multiple combined \n'
                'years of learning and experience.\n'
                ' Please note that some of these \n'
                'options require API keys. The labels \n'
                'are representative of the \n'
                'site you can get the keys from. \n\n'
                'Thank you for supporting SwipeDown, \n'
                'and we hope you enjoy this toolkit!\n\n\n'
                'My available directives are as follows:')
    strings = [
        'Advice',
        'Calculator',
        'Camera',
        'Discord',
        'Email',
        'Google Search',
        'Your IP',
        'Dad Jokes',
        'Trending Movies',
        'Global News',
        'Notepad (default for your system',
        'Open Powershell',
        'Toolkit of Destiny',
        'Weather',
        'Send a WhatsApp text',
        'Wikipedia Search',
        'YouTube video'
    ]
    menu = SelectionMenu(
        clear_screen=True,
        title=title,
        subtitle=subtitle,
        strings=strings,
        show_exit_option=True,
        exit_option_text='[+] Quit'
    )

    selection = input(f'Please enter 0 to begin: ')
    match selection:
        case '0':
            print('Please choose a number between 1 and 17, the menu will continue from there.')
        case '1':
            import SwipeDown.JARVIS.functions.online_utility.advice as advice
            wikipedia = FunctionItem('[+] Advice', advice.main())
            menu.append_item(wikipedia)
        case '2':
            import SwipeDown.JARVIS.functions.local_utility.calculator as calculator
            calc = FunctionItem('[+] Calculator', calculator.main())
            menu.append_item(calc)
        case '3':
            import SwipeDown.JARVIS.functions.local_utility.camera as camera
            cam = FunctionItem('[+] Camera', camera.main())
            menu.append_item(cam)
        case '4':
            import SwipeDown.JARVIS.functions.local_utility.discord as discord
            disc = FunctionItem('[+] Discord', discord.main())
            menu.append_item(disc)
        case '5':
            import SwipeDown.JARVIS.functions.online_utility.send_email as email
            send_email = FunctionItem('[+] Email', email.main())
            menu.append_item(send_email)
        case '6':
            import SwipeDown.JARVIS.functions.online_utility.google as google
            search_google = FunctionItem('[+] Google', google.main())
            menu.append_item(search_google)
        case '7':
            import SwipeDown.JARVIS.functions.online_utility.ip as ip
            get_ip = FunctionItem('[+] IP', ip.main())
            menu.append_item(get_ip)
        case '8':
            import SwipeDown.JARVIS.functions.online_utility.joke as joke
            get_jokes = FunctionItem('[+] Jokes', joke.main())
            menu.append_item(get_jokes)
        case '9':
            import SwipeDown.JARVIS.functions.online_utility.trending_movies as movies
            get_movies = FunctionItem('[+] Movies', movies.main())
            menu.append_item(get_movies)
        case '10':
            import SwipeDown.JARVIS.functions.online_utility.News.main as news
            get_news = FunctionItem('[+] News', news.main())
            menu.append_item(get_news)
        case '11':
            import SwipeDown.JARVIS.functions.local_utility.notepad as notepad
            get_notepad = FunctionItem('[+] Notepad', notepad.main())
            menu.append_item(get_notepad)
        case '12':
            import SwipeDown.JARVIS.functions.local_utility.open_powershell as powershell
            powershell_sesh = FunctionItem('[+] Powershell', powershell.main())
            menu.append_item(powershell_sesh)
        case '13':
            import destiny.toolkit as destiny
            run_toolkit = FunctionItem('[+] Toolkit of Destiny', destiny.main())
            menu.append_item(run_toolkit)
        case '14':
            import SwipeDown.JARVIS.functions.online_utility.weather as weather
            get_weather = FunctionItem('[+] Weather', weather.main())
            menu.append_item(get_weather)
        case '15':
            import SwipeDown.JARVIS.functions.online_utility.whatsappmessage as whatsapp
            text = FunctionItem('[+] WhatsApp', whatsapp.main())
            menu.append_item(text)
        case '16':
            import SwipeDown.JARVIS.functions.online_utility.wiki as wiki
            wikipedia = FunctionItem('[+] Wikipedia', wiki.main())
            menu.append_item(wikipedia)
        case '17':
            import SwipeDown.JARVIS.functions.online_utility.playonyt as yt
            youtube = FunctionItem('[+] YouTube', yt.main())
            menu.append_item(youtube)

    menu.show()

if __name__ == '__main__':
    main()
