import networkx as nx
import time
from RCM import RCM
from Fiedler import Fiedler
import scipy.io as sio
import os

# Generate seed For gnp_random_graph
SEED = int(time.time())

# G = nx.gnp_random_graph(1000, .00001, SEED)
# G = nx.gnp_random_graph(10000, .00001, SEED)
# G = nx.gnp_random_graph(100000, .0001, SEED)
# G = nx.gnp_random_graph(1000000, .0001, SEED)


def get_neighbors(adjacency_matrix, node):

    if node < 0 or node >= len(adjacency_matrix):
        # Node index out of bounds
        return []

    neighbors = []
    for i in range(len(adjacency_matrix[node])):
        if adjacency_matrix[[node], [i]] != 0:
            neighbors.append(i)

    return neighbors



if __name__=='__main__':
    
    # RCM_G = RCM(G)
    # Fiedler_G = Fiedler(G).todense()

    # # G = G.todense()
    # GRAPH_SIZE = len(G)

    # os.makedirs('data', exist_ok=True)
    # A = nx.adjacency_matrix(G)

    # sio.mmwrite(f'data/normal_{GRAPH_SIZE}.mtx', A)
    # sio.mmwrite(f'data/Fiedler_{GRAPH_SIZE}.mtx', Fiedler_G)
    # sio.mmwrite(f'data/RCM_{GRAPH_SIZE}.mtx', RCM_G)

    G = sio.mmread('data/Fiedler_10000.mtx').todense()

    for i in range(len(G)):
        get_neighbors(G, i)
