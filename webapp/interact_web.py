import re
import requests
import json



sites = [" https://newsapi.org/v1/articles?source=the-new-york-times&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=the-washington-post&sortBy=top&apiKey={}".format( '84c3c49e152c42f48b212cff473a9397'),
"https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
" https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=financial-times&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=national-geographic&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=new-scientist&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=newsweek&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=new-york-magazine&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=the-economist&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=the-guardian-au&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=the-wall-street-journal&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
"https://newsapi.org/v1/articles?source=time&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397",
" https://newsapi.org/v1/articles?source=usa-today&sortBy=top&apiKey=84c3c49e152c42f48b212cff473a9397"]



def nyt_past_articles():
   r = requests.get("https://api.nytimes.com/svc/archive/v1/2016/1.json?api-key={}".format("0587221535c5449193d34683545dd05a"))
   print(r._content)


def get_headlines():
    headlines = []
    for s in sites:
        r = requests.get(s)

        content = json.loads(r._content.decode('utf8'))
        for k,v in content.items():
            for a in content['articles']:
                headlines.append(a['title'])

    return headlines





