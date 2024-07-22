from consolemenu import ConsoleMenu, FunctionItem
from datetime import datetime
from SwipeDown.JARVIS.functions.online_utility.News.news import *
from SwipeDown.keys import news

def display_news():
    API_KEY = news  # Replace with your actual News API key

    now_local = datetime.now()
    local_time = now_local.strftime('%Y-%m-%d')
    print("Current local time:", local_time)

    set_q = input('What would you like news about? ')
    set_sources = input('Where do you want it from? ')
    from_param = input('Would you like today\'s news? (yes/no) ').strip().lower()

    if from_param == 'yes':
        from_param = local_time
        to_param = local_time
    else:
        from_param = input('When do you want news from? (YYYY-MM-DD) ')
        to_param = input('When do you want news to? (YYYY-MM-DD) ')

    top_headlines, all_articles = get_latest_news(API_KEY, set_q, set_sources, from_param, to_param)
    formatted_headlines = format_articles(top_headlines)
    formatted_articles = format_articles(all_articles)

    print("\nTop Headlines:\n")
    for article in formatted_headlines:
        print(article)

    print("\nAll Articles:\n")
    for article in formatted_articles:
        print(article)


def main():
    menu = ConsoleMenu("News Menu", "Select an option:")
    news_item = FunctionItem("Get Latest News", display_news)
    menu.append_item(news_item)
    menu.show()


if __name__ == '__main__':
    main()
