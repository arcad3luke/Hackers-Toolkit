import subprocess as sp
import SwipeDown.SwipeDown.JARVIS.functions.os_ops as os_ops
from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu

def open_calculator():
    sp.Popen(os_ops.paths['calculator'])

def main():
    show_menu = ConsoleMenu(title='Open the calculator!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    news = FunctionItem('[+] Open the calculator!', open_calculator())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(news)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()