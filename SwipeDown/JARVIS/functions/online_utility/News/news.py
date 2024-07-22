from newsapi import NewsApiClient


def get_latest_news(api_key, query, sources, from_date, to_date):
    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines(q=query, sources=sources, language='en')
    all_articles = newsapi.get_everything(q=query, sources=sources, from_param=from_date, to=to_date, language='en',
                                          sort_by='relevancy')

    return top_headlines, all_articles


def format_articles(articles):
    formatted_articles = []
    for article in articles['articles']:
        formatted_article = f"{article['title']}\n{article['description']}\n{article['url']}\n"
        formatted_articles.append(formatted_article)
    return formatted_articles
