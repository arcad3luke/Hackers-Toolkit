import platform

import SwipeDown.SwipeDown.swipedown as sd


def os_check(client):
    if platform.system() == 'Linux':
        print(f'The current OS is Linux, it\'s version is: {platform.release()}')
    elif platform.system() == 'Darwin':
        print(f'The current OS is MacOS, it\'s version is: {platform.release()}')
    elif platform.system() == 'Windows':
        print(f'The current OS is Windows, it\'s version is: {platform.release()}')

client = sd.client
os_check(client=client)

if __name__ == '__main__':
    os_check(client)