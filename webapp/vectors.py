import numpy as np
import scipy
from sklearn.feature_extraction.text import CountVectorizer
import re



class ConfirmedHeadlines(object):

    def __init__(self, twitterlines, weblines, inputlines):
        super(ConfirmedHeadlines, self).__init__()

        self.unified = weblines + twitterlines + inputlines
        self.inputlines = inputlines
        self.headlines = self.unified

        self.matrix = self.make_matrix()

    def make_matrix(self):
        vectorizer = CountVectorizer(min_df=1)

        return vectorizer.fit_transform(self.headlines)


class SourcedHeadlines(object):

    def __init__(self, corpus_lines, input):
        super(SourcedHeadlines, self).__init__()

        self.corpus_lines = corpus_lines + list(input)
        self.matrix = self.make_matrix()

    def make_matrix(self):
        vectorizer = CountVectorizer(min_df=1)

        return vectorizer.fit_transform(self.corpus_lines)

class TrainHeadlines(object):
    def __init__(self, headlines, input):
        super(TrainHeadlines, self).__init__()

        self.headlines = headlines + input

        self.matrix = self.make_matrix()

    def make_matrix(self):
        vectorizer = CountVectorizer(min_df=1)
        return vectorizer.fit_transform(self.headlines)
