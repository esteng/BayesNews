import numpy as np
import sys

def all_dist(matrix):
    all_dists = []
    last_row =  matrix[-1,:]
    for i in range(0, matrix.shape[0]-2):
        all_dists.append(cosine_dist(matrix[i,:], last_row))
    return all_dists
def cosine_dist(X, Y):

    dotprod = np.dot(X,Y)
    denom = np.linalg.norm(X)*np.linalg.norm(Y)

    return 1-dotprod/denom