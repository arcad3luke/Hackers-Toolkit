import pywhatkit as kit
from consolemenu import *
from consolemenu.items import *


def send_whatsapp_message(area_code, number, message):
    kit.sendwhatmsg_instantly(f'+{area_code} {number}', message)

def main():
    import SwipeDown.SwipeDown.Menu.menu as menu
    show_menu = ConsoleMenu('Welcome to the Whatsapp module, press 1 to send a text,\n 2 to go back, \nand 3 to exit!',
                            show_exit_option=True, exit_option_text='[+] Quit')
    whatsapp_function = FunctionItem('[+] Send an Text', send_whatsapp_message(area_code = input('Enter area code: '),
                                                                               number=input('what phone number would you like to use?'),
                                                                               message=input('What would you like to say?')))
    back_function = FunctionItem('[+] Back', menu.main)

    show_menu.append_item(whatsapp_function)
    show_menu.append_item(back_function)
    show_menu.show()

if __name__ == '__main__':
    main()
