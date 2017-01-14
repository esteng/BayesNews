from distance import get_prior, get_marginal, get_likelihood


def bayes(twits, webs, input):
    print("inside bayes")
    prior = get_prior(twits, webs, input)
    likelihood = get_likelihood(input)
    marginal = get_marginal(twits, webs, input)
    posterior = ((1-prior)*likelihood)/marginal
    boolean = "TRUE" if 1-posterior > .5 else "FALSE"
    print(input[0:20], "... is ", boolean)

    return (prior, likelihood, marginal, posterior, 1-posterior)












