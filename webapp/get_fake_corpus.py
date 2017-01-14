import requests
import re
import json


sources = {"http://abcnews.com.co/news/news/":["<div class=\"td-module-thumb\">.*?title=.*?>", "(?<=(title=\")).*?(?=\")"],
 "http://thebostontribune.com/":["<div class=\"td-module-thumb\">.*?title=.*?>", "(?<=(title=\")).*?(?=\")"],
 "http://creambmp.com/":["<h1 class=\"entry-title\".*<\/h1>","(?<=(title=\")).*?(?=\")"],
 "http://civictribune.com/":["<li class=\"newsframe-item\">[^&]*<\/li>","(?<=(title=\")).*?(?=\")"]}


def get_fake(source, art, title):

    headlines = []
    try:
        article_regex = re.compile(art)
        title_regex = re.compile(title)

        r = requests.get(source)
        all_articles = article_regex.findall(r._content.decode("utf8"))
        for art in all_articles:

            headline_match = title_regex.search(art)
            if headline_match is not None:
                headlines.append(headline_match.group(0))
    except:
        pass
    return headlines



def get_all():
    with open("lists/fake_headlines", "a") as f1:
        for k,v in sources.items():
            headlines = get_fake(k, v[0],v[1])
            for h in headlines:
                f1.write(h + "\n")

