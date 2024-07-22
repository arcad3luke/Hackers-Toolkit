import os
import SwipeDown.SwipeDown.JARVIS.functions.os_ops as os_ops
from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu

def open_notepad():
    os.startfile(os_ops.paths['notepad'])

def main():
    show_menu = ConsoleMenu(title='Open Notepad!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    notepad = FunctionItem('[+] Open Notepad!', open_notepad())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(notepad)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()