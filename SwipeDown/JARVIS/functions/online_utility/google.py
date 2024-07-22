import pywhatkit as kit
import SwipeDown.SwipeDown.Menu.menu as menu
from consolemenu import *
from consolemenu.items import *

def searchgoogle(query):
    kit.search(query)

def main():
    show_menu = ConsoleMenu(title='Search Google!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    google = FunctionItem('[+] Search Google', searchgoogle(query=input('What is your search query?')))
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(google)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()