import subprocess as sp
from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def main():
    show_menu = ConsoleMenu(title='Get the latest news!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    camera = FunctionItem('[+] Get the latest news', open_camera())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(camera)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()