#BayesNews
-----------
BayesNews is a "fake news" detector based on real-time Bayesian inference. The underlying intuition is that for any given real news story, multiple outlets will report on it. This means that the veracity of a headline can be determined within a time-frame based on what other sources are talking about (given an important and globally relevant headline). While other approaches have attempted to detect fake news based on a variety of data, BayesNews attempts to determine the veracity based solely on the content of the headline. Thus certain limitations apply such as 

- **time**: given a headline from several years ago, there will be little corroborating reporting at the moment.
- **relevance**: local news is more likely to be designated fake than global news. The smaller impact the headline, the more likely it is not to be fake.
- **wording**: peculiar or informal wording will work against a headline, as real headlines used for comparison are sourced from respected sources which often use very similar writing styles.
