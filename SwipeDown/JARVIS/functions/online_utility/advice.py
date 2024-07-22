import requests
import SwipeDown.SwipeDown.Menu.menu as menu
from consolemenu import *
from consolemenu.items import *

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

get_random_advice()

def main():
    show_menu = ConsoleMenu(title='Get the latest advice!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    advice = FunctionItem('[+] Get the latest advice', get_random_advice())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(advice)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()