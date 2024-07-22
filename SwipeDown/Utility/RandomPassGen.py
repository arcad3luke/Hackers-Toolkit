from consolemenu import *
from consolemenu.items import *

def random_pass_gen():
    import random
    import sys
    passlen = int(input('enter the length of the password: '))
    s='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]\\{}|:";\',./<>?'
    p = "".join(random.sample(s, passlen))
    print(p)
    run_again = input('Wanna run again? (y/n)')
    if run_again.upper() == 'Y':
        random_pass_gen()
    else:
        sys.exit()

def main():
    import SwipeDown.SwipeDown.Menu.menu as menu

    show_menu = ConsoleMenu('Generate a random password!', show_exit_option=True, exit_option_text='[+] Quit')
    rand_pass = FunctionItem('[+] Random Password', random_pass_gen())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(rand_pass)
    show_menu.append_item(back)
    show_menu.show()