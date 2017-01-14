from interact_twitter import get_tweets
from interact_web import get_headlines
from vectors import ConfirmedHeadlines
from sklearn.feature_extraction.text import CountVectorizer
from scipy import spatial
import numpy as np


# vectorizer = CountVectorizer(min_df=1)

input_string = ["Hillary Clinton has body double."]
# input_vector = vectorizer.fit_transform(input_string)

# twits = get_tweets()

# twits = ["Hillary Clinton has corporal double"]
# webs = ["Michael Jackson found dead at 43"]

twits = [ 'Inside this mental hospital in Venezuela, psychiatric patients face shortages of food and medicine… ', 'RT  Showtime! #theapprentice ', 'RT  Andy Murray named BBC Sports Personality of the Year. 🏆 Details of all awards:  ', "Trump aide plays down prospect of upending 'one China' policy  ", 'RT  Congratulations Alistair Brownlee 🏆\n\nSecond place in BBC Sports Personality of the Year 2016. \n\n #SPOT…', 'RT  As they watch Donald #Trump’s transition to the White House, supporters say “We have to trust him.” ', "RT  It's history for Andy Murray!\n\nHe's the first person to win BBC's Sports Personality of the Year three times.\n\n🏆 Congratulati…", 'RT  What a year it has been for Nick Skelton! 🏆\n\nThird place in the BBC Sports Personality of the Year 2016. \n\n', '900,000 children have been displaced by the on-going war in South Sudan  ', 'BLT Prime review: Trump Hotel’s steakhouse does plenty of things right ', '"I love you." She had said it.\nAt first, he didn\'t say anything. Then, finally, he muttered, "Thank you."\n', "RT  We'll bring you the announcement live from  and have reaction from the award winners\n\n http…", 'RT  What an unbelievable and magical season they had!\n\n🏆 Congratulations Leicester City 🏆\n\n➡️  #LCFC #SPOT…', 'Denied justice, this Italian Renaissance painter channeled her rape into her art ', 'At Least 10 Die In Shootout At Crusader Castle In Jordan ']
webs = get_headlines()

cfhl = ConfirmedHeadlines(twits, webs, input_string)

print(cfhl.matrix.toarray())

print(spatial.distance.pdist(cfhl.matrix.toarray(), metric = 'cosine'))

X = spatial.distance.squareform(spatial.distance.pdist(cfhl.matrix.toarray(), metric = 'cosine'))
# print(X)

ind =  len(cfhl.unified) - len(cfhl.inputlines)
lastvect = X[ind,:]

minval = 2.0
index =0
print(lastvect)
for i,e in enumerate(lastvect):
    if i == len(X)-1: 
        break
    if e < minval:
        minval = e
        index = i 

print(minval, index)
unified = webs+twits+input_string

print(unified[index])

print("similarity is : ", 1-minval)
