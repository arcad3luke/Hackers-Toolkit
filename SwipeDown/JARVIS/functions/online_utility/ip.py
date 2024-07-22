from consolemenu import *
from consolemenu.items import *
import time
import requests
import SwipeDown.SwipeDown.Menu.menu as menu


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except requests.RequestException:
        return None


def main():
    # Start the timer
    start_time = time.time()

    public_ip = get_public_ip()
    if public_ip:
        print("Public IP Address:", public_ip)
    else:
        print("Unable to retrieve public IP.")

    # End the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Report the timing
    print("Execution time: {:.2f} seconds".format(elapsed_time))


    show_menu = ConsoleMenu('Welcome to the IP module, press 1 to grab your IP, 2 to go back, and 3 to exit!',
                            show_exit_option=True, exit_option_text='[+] Quit')
    ip_function = FunctionItem('[+] Get IP', get_public_ip)
    back_function = FunctionItem('[+] Back', menu.main)

    show_menu.append_item(ip_function)
    show_menu.append_item(back_function)
    show_menu.show()


if __name__ == '__main__':
    main()
