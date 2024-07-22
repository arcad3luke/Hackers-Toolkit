import os

from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.JARVIS.functions.os_ops as os_ops
import SwipeDown.SwipeDown.Menu.menu as menu

def open_discord():
    os.startfile(os_ops.paths['discord'])

def main():

    show_menu = ConsoleMenu('Welcome to the Discord module, press 1 to launch Discord, 2 to go back, and 3 to exit!',
                            show_exit_option=True, exit_option_text='[+] Quit')
    discord_function = FunctionItem('[+] Open Discord', open_discord)
    back_function = FunctionItem('[+] Back', menu.main)

    show_menu.append_item(discord_function)
    show_menu.append_item(back_function)
    show_menu.show()