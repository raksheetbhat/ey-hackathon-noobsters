import requests
import json
import copy

from newspaper import Article

CSE_MAP = {
    "BCG":"9ed0c8dc4ee97eed6",
    "MCKINSEY":"1217f499159cde689",
    "delloite":"",
    "KPMG" : "",
    "PWC" : ""
}


SEARCH_SCHEMA = {
    "link": "",
    "title": "",
    "text": "",
    "summary": "",
    "keywords": ""
}

KEY = 'AIzaSyAYEhqHdTRhptnlGghVhah6ntitnxtOzZU'


def get_custom_search_results(company, keyword):

    print("Fetching custom website results for : " + company + " " + keyword)

    search_engine = CSE_MAP.get(company)

    if search_engine is None:
        return []

    query_string = {'key': KEY,
             'cx':search_engine,
             'q':'"' + keyword + '"',
             'sort':'date'}

    r = requests.get('https://www.googleapis.com/customsearch/v1',params=query_string)

    output = []

    if r.status_code == 200:

        print('success')

        response = json.loads(r.text)

        for item in response["items"]:
            article = get_article(item["link"])

            if article is not None:
                # print("Title : " + article.title)
                # print("Publish date : " + str(article.publish_date))
                # print("Author : " + str(article.authors))
                # print("Keywords : " + str(article.keywords))
                # print("Text : " + str(article.text))
                # print("\n")

                search = copy.deepcopy(SEARCH_SCHEMA)

                search["title"] = str(article.title)
                search["link"] = item["link"]
                search["keywords"] = str(article.keywords)
                search["summary"] = str(article.summary)
                search["text"] = str(article.text)

                output.append(search)

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


# print(get_custom_search_results('BCG','Supply chain'))
