import time
from RCM import RCM
from Fiedler import Fiedler
import scipy.io as sio
import os
import scipy.sparse as ss

# Generate seed For gnp_random_graph
# SEED = int(time.time())

# G_1000 = ss.random(1000, 1000, density=0.0001, format='csr', random_state=42)
# G_10000 = ss.random(10000, 10000, density=0.0001, format='csr', random_state=42)
# G_100000 = ss.random(100000, 100000, density=0.00000001, format='csr', random_state=42)
# G_1000000 = ss.random(1000000, 1000000, density=0.00000001, format='csr', random_state=42)

# Load G
G_1000 = ss.load_npz('data/G_1000.npz')
# RCM_G_1000 = ss.load_npz('data/RCM_G_1000.npz')
# Fiedler_G_1000 = ss.load_npz('data/Fiedler_G_1000.npz')
# G_10000 = ss.load_npz('data/G_1000.npz')
# RCM_G_10000 = ss.load_npz('data/RCM_G_1000.npz')
# Fiedler_G_10000 = ss.load_npz('data/Fiedler_G_1000.npz')

def get_neighbors(csr_matrix, node):

    if node < 0 or node >= csr_matrix.getnnz():
        # Node index out of bounds
        return

    start = csr_matrix.indptr[node]
    end = csr_matrix.indptr[node+1]
    return csr_matrix.indices[start:end]



if __name__=='__main__':
    G = G_1000
    for i in range(G.getnnz()):
        print(get_neighbors(G, i))



    for i in range(len(G)):
        get_neighbors(G, i)
