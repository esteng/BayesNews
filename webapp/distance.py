from interact_twitter import get_tweets
from interact_web import get_headlines
from vectors import ConfirmedHeadlines, SourcedHeadlines,TrainHeadlines
from cosine import all_dist
import sys
import os



def get_prior(twits, webs, input):
    
    cfhl = ConfirmedHeadlines(twits, webs, [input])
    lastvect = cfhl.matrix.toarray()
    resultsvect = all_dist(cfhl.matrix.toarray())

    minval = 2.0
    index =0
    for i,e in enumerate(resultsvect):
        if e < minval:
            minval = e
            index = i 

    # print(minval, index)
    unified = webs+twits+[input]

    # print(unified[index])

    print("prior is : ", 1-minval)
    return 1-minval


def get_marginal(twits, webs, input):
    headlines = twits+webs
    

    shl = SourcedHeadlines(headlines, [input])
    # X = spatial.distance.squareform(spatial.distance.pdist(shl.matrix.toarray(), metric = 'cosine'))

    # ind =  X.shape[0]-1
    # lastvect = X[ind,:]
    lastvect = shl.matrix.toarray()
    resultsvect = all_dist(shl.matrix.toarray())
    minval = 2.0
    index =0


    for i,e in enumerate(resultsvect):

        if e < minval:
            minval = e
            index = i 

    unified = headlines+[input]
    # print(unified[index])
    print("marginal is : ", 1-minval)
    return 1-minval

def get_likelihood(input):

    # with open(os.path.join(os.path.split(os.path.realpath(__file__))[0],"fake_headlines")) as f1:
    with open("lists/fake_headlines") as f1:
        fake_headlines = list(set([x.strip() for x in f1.readlines()]))

    thl = TrainHeadlines(fake_headlines, [input])

    lastvect = thl.matrix.toarray()
    resultsvect = all_dist(thl.matrix.toarray())

    # X = spatial.distance.squareform(spatial.distance.pdist(thl.matrix.toarray(), metric = 'cosine'))

    # ind =  X.shape[0]-1
    # lastvect = X[ind,:]

    minval = 2.0
    index =0


    for i,e in enumerate(resultsvect):
        # if i == len(X)-1: 
        #     break
        if e < minval:
            minval = e
            index = i 

    unified = fake_headlines+[input]
    # print(unified[index])
    print("likelihood is : ", 1-minval)
    return 1-minval


# print(get_likelihood("StreetScore scores a street view based on how safe it looks to a human"))
# print(get_likelihood("At Least 9 Dead After Truck Plows Into Christmas Market In Berlin"))
