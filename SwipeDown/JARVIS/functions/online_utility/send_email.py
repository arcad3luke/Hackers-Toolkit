import socket
from consolemenu import *
from consolemenu.items import *


def get_internal_ip():

    try:
        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as  s:
            # Connect to a known external server
            s.connect(('8.8.8.8', 80))

        # Get the socket name (including the local IP address)
            internal = s.getsockname()[0]
        return internal
    except socket.error:
        # Error occurred, return None or handle it as desired
        return None
    finally:
        # Close the socket
        s.close()

# Call the function to get the internal IP
get_internal_ip()

def send_email():
    import os
    import smtplib, ssl
    import requests

    login = os.getlogin()
    sys_info = os.getenv('os')
    ip = get_internal_ip()
    public_ip = requests.get('http://ipv4.icanhazip.com').text.strip('\n')
    print(public_ip)
    print(ip)
    print(login)
    print(sys_info)

    port = 465  # For SSL
    email = input('Type your email and press enter: ')
    password = input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.sendmail(from_addr=email, to_addrs=email, msg=f'{login} | {sys_info} | {ip} | {public_ip}')

def main():
    import SwipeDown.SwipeDown.Menu.menu as menu
    show_menu = ConsoleMenu('Welcome to the Email module, press 1 to send an email , 2 to go back, and 3 to exit!',
                            show_exit_option=True, exit_option_text='[+] Quit')
    email_function = FunctionItem('[+] Send an Email', send_email())
    back_function = FunctionItem('[+] Back', menu.main)

    show_menu.append_item(email_function)
    show_menu.append_item(back_function)
    show_menu.show()

if __name__ == '__main__':
    main()
