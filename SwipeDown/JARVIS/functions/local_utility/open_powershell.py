import os
from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu

def open_powershell():
    os.system('start powershell')

def main():
    show_menu = ConsoleMenu(title='Open Powershell!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    powershell = FunctionItem('[+] New powershell session', open_powershell())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(powershell)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()