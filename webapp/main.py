from bayes import bayes
from interact_web import get_headlines
from interact_twitter import get_tweets
from get_fake_corpus import get_all
import csv
import sys


if __name__ == '__main__':
    get_all()
    twits = get_tweets()
    with open("lists/real_headlines","r") as f1:
        real_lines = list(set(f1.readlines())) #remove duplicates
    webs = get_headlines()+real_lines

    with open("lists/test") as f1:
        lines = [x.strip() for x in f1.readlines()]


    f2 = open("test_results.csv", "w") 
    f2cw = csv.writer(f2)
    f2cw.writerow(["prior", "likelihood", "marginal", "posterior", "probability", "value"])
    for line in lines:
        towrite = list(bayes(twits, webs, line))
        if towrite[-1] > .5:
            towrite.append("True")
        else:
            towrite.append("False")
        f2cw.writerow(towrite)
