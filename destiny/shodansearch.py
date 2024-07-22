import keys
import shodan
from consolemenu import *
from consolemenu.items import *
import toolkit

def shodanmodule():
    api = shodan.Shodan(keys.keys['shodankey'])
    print('Welcome to our Shodan Module')
    search = input("\nSearch query:")
    print("\nSearching...")
    results = api.search(search)
    print('\nResults found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')

def main():
    menu = ConsoleMenu("Welcome to the Shodan module", "Choose to launch or go back", show_exit_option=True,
                       exit_option_text='[+] Quit')
    Shodan_function = FunctionItem('[+] Search Shodan', shodanmodule)
    Back_function = FunctionItem('[+] Back', toolkit.main())
    show_main_menu = FunctionItem('[+] Main Menu', main_menu.main())
    menu.append_item(Shodan_function)
    menu.append_item(Back_function)
    menu.append_item(show_main_menu)
    menu.show()

if __name__  == '__main__':
    main()