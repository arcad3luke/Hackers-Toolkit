# def bullshit():
#     i = random.randint(0, 100)
#     if 0 <= i <= 25:
#         print(f'low range number: {i}')
#     elif 26 <= i <= 50:
#         print(f'medium range number: {i}')
#     elif 51 <= i <= 75:
#         print(f'upper range number: {i}')
#     elif 76 <= i <= 100:
#         print(f'high range number: {i}')
#     else:
#         print('No Numbers!')
#
# bullshit()

import socket


def get_internal_ip():
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM)as s:

        try:
            # Connect to a known external server
            s.connect(('8.8.8.8', 80))

            # Get the socket name (including the local IP address)
            internal_ip = s.getsockname()[0]
            return internal_ip
        except socket.error:
            # Error occurred, return None or handle it as desired
            return None
        finally:
            # Close the socket
            s.close()

# Call the function to get the internal IP
internal_ip = get_internal_ip()

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

def flask_api():
    import flask
    from flask import jsonify, render_template
    @app.route('/quests()', methods=['GET'])
    def get_quests():
        quest_Query = Quest.query.all()
        quests = {}
        for quest in quest_Query:
            quests[quest.name] = quest.description
        return jsonify(quests)


def main():
    #send_email()
    random_pass_gen()

if __name__ == '__main__':
    main()