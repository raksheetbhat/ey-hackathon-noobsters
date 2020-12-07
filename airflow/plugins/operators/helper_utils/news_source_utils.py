from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
import requests
from newspaper import Article

import copy

NEWS_SCHEMA = {
    "title": "",
    "link": "",
    "date": "",
    "authors": "",
    "keywords": "",
    "summary": "",
    "text": ""
}


def get_news_articles(keyword):

    print("starting news scraping : " + keyword)

    googlenews = GoogleNews(lang='en', period='7d')
    googlenews.search(keyword)

    links = googlenews.get_links()
    googlenews.clear()

    print(links)

    output = []

    for link in links:

        article = get_article(link)

        if article is not None:
            news = copy.deepcopy(NEWS_SCHEMA)
            news["title"] = str(article.title)
            news["link"] = link
            news["date"] = str(article.publish_date)
            news["keywords"] = str(article.keywords)
            news["summary"] = str(article.summary)
            news["text"] = str(article.text)
            news["authors"] = str(article.authors)

            output.append(news)

    return output


def get_article(link):

    article = Article(link)

    try:
        article.download()
        article.parse()
        article.nlp()

    except Exception as e:
        print(e)
        article = None

    return article

#
# article = get_article('https://www.linkedin.com/pulse/5-biggest-retail-trends-2021-bernard-marr/')
# print(article.text)











