import scipy
from scipy.sparse.linalg import eigs
from scipy.sparse import csr_matrix
import networkx as nx
import numpy as np


def Fiedler(G):
    '''
    Reorder a graph according to Fiedler vector heuristic.
    The fiedler vector is the second smallest eigenvector of the Laplacian matrix.

    Parameters: G -> type: matrix

    Returns: Fiedler_A -> type: matrix

    '''

    # If G is in csr format, convert to dense, then compute adjacency matrix
    # if type(G) == scipy.sparse._csr.csr_array:
    #     G = G.todense()
    # A = nx.adjacency_matrix(G)

    # Compute the Laplacian matrix
    L = scipy.sparse.csgraph.laplacian(G)
    
    # Find first 2 eigenvectors
    _, eig_vectors = eigs(L.astype('float64'), k=2, which='SM', maxiter=3000, tol=0.01)

    # Select second eigen vector
    Fiedler_vector = np.argsort(eig_vectors[:, 1])

    # Reorder nodes according to the second eigenvector
    Fiedler_G = G[Fiedler_vector, Fiedler_vector]

    return Fiedler_G

