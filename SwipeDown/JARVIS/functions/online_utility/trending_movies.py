import requests
import os
from consolemenu import *
from consolemenu.items import *
import SwipeDown.SwipeDown.Menu.menu as menu


def get_trending_movies():
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res[""]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

def main():
    show_menu = ConsoleMenu(title='Search the movie database!', clear_screen=True,
                            show_exit_option=True, exit_option_text='[+] Quit')
    movie = FunctionItem('[+] Search for a movie', get_trending_movies())
    back = FunctionItem('[+] Back', menu.main())
    show_menu.append_item(movie)
    show_menu.append_item(back)
    show_menu.show()

if __name__ == '__main__':
    main()