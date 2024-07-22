from consolemenu import *
from consolemenu.items import *
import zdstresser
import nmapmodule
import shodansearch


def main():
    menu = ConsoleMenu("Welcome to our toolkit!", "Some modules require API keys. Reference keys.py.", show_exit_option=True,
                       exit_option_text='[+] Quit')
    nmap_function = FunctionItem('[+] Nmap', nmapmodule.main())
    shodan_function = FunctionItem('[+] Shodan Search', shodansearch.main())
    zdstresser_function = FunctionItem('[+] Zdstresser.net DDOS Module (Requires API key)', zdstresser.main())
    main_menu = FunctionItem('[+] SwipeDown Main Menu', show_main_menu.main())
    menu.append_item(nmap_function)
    menu.append_item(shodan_function)
    menu.append_item(zdstresser_function)
    menu.append_item(main_menu)

    menu.show()


if __name__ == '__main__':
    main()