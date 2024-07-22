import wikipedia
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
import SwipeDown.SwipeDown.Menu.menu as menu


def search_wikipedia():
    search_query = input("Enter your search query: ")
    try:
        result = wikipedia.summary(search_query)
        print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
    except wikipedia.exceptions.PageError as e:
        print(e)

def main():
    show_menu = ConsoleMenu(title='Search Wikipedia!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    wiki = FunctionItem('[+] Search Wikipedia', search_wikipedia())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(wiki)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()