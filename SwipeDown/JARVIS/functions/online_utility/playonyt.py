from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu
import pywhatkit as kit

def playonyt(video):
    kit.playonyt(video)

def main():
    show_menu = ConsoleMenu(title='Play a YouTube video', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    youtube = FunctionItem('[+] Search for a video', playonyt(video=input('What kind of video do you want to see?')))
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(youtube)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()