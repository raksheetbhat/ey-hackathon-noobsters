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

    print("starting news scraping")

    googlenews = GoogleNews(lang='en', period='7d')
    googlenews.search(keyword)

    links = googlenews.get_links()
    googlenews.clear()

    print(links)

    output = []

    for link in links:

        article = get_article(link)

        if article is not None:
            # print("Title : " + article.title)
            # print("Publish date : " + str(article.publish_date))
            # print("Author : " + str(article.authors))
            # print("Keywords : " + str(article.keywords))
            # print("Summary : " + str(article.summary))

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


def scrap_news_article(link):

    print("Requesting news article")

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    })

    response = requests.get(link, allow_redirects=True, headers = headers)

    html_page = response.content

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    # print(text)

    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'a',
        'script',
        '!--',
        # there may be more elements you don't want, such as "style", etc.
    ]

    whitelist = [
        'div',
        'p',
        'ul',
        'li',
        'ol',
    ]

    output = []

    for t in text:
        if t.parent.name in whitelist and t is not None and t != "" and len(t) > 50:
            output.append(t)

    return output

#
# article = get_article('https://www.linkedin.com/pulse/5-biggest-retail-trends-2021-bernard-marr/')
# print(article.text)











