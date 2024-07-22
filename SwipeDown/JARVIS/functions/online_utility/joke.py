import requests
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from SwipeDown.Menu import menu


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()

    limit = 3
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'REDACTED'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return res["joke"]

def main():
    show_menu = ConsoleMenu(title='Get a few jokes!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    joke = FunctionItem('[+] Get 3 jokes', get_random_joke)
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(joke)
    show_menu.show()

if __name__ == '__main__':
    main()
