import time
from RCM import RCM
from Fiedler import Fiedler
import scipy.io as sio
import scipy.sparse as ss
from BPL import bits_per_link

# Generate seed For gnp_random_graph
# SEED = int(time.time())

# G_1000 = ss.random(1000, 1000, density=0.0001, format='csr', random_state=42)
# G_10000 = ss.random(10000, 10000, density=0.0001, format='csr', random_state=42)
# G_100000 = ss.random(100000, 100000, density=0.00000001, format='csr', random_state=42)
# G_1000000 = ss.random(1000000, 1000000, density=0.00000001, format='csr', random_state=42)

# Load G
# G_DATA = ss.load_npz('data/data.npz')
# RCM_G_1000 = ss.load_npz('data/RCM_G_1000.npz')
# Fiedler_G_1000 = ss.load_npz('data/Fiedler_G_1000.npz')
# G_10000 = ss.load_npz('/work/acslab/users/manning/489Project/data/G_10000_0000001.npz')
# RCM_G_10000 = ss.load_npz('data/RCM_G_10000_0000001.npz')
Fiedler_G_10000 = ss.load_npz('data/Fiedler_G_10000_0000001.npz')

def get_neighbors(csr_matrix, node):

    if node < 0 or node >= csr_matrix.shape[0]:
        # Node index out of bounds
        return []

    start = csr_matrix.indptr[node]
    end = csr_matrix.indptr[node+1]
    return csr_matrix.indices[start:end]

def get_second_order_neighbors(csr_matrix, node):
    second_order_neighbors = set()
    first_order_neighbors = set(get_neighbors(csr_matrix, node))

    for neighbor in first_order_neighbors:
        # Exclude the original node and its first-order neighbors
        neighbors_of_neighbor = set(get_neighbors(csr_matrix, neighbor))
        second_order_neighbors.update(neighbors_of_neighbor)

    # Remove the original node and its first-order neighbors
    second_order_neighbors.difference_update(first_order_neighbors, {node})

    return list(second_order_neighbors)
    


if __name__=='__main__':

    G = Fiedler_G_10000
    print(len(G.nonzero()[0]))
    print(bits_per_link(G))

    start = time.time()
    for i in range(G.getnnz()):
        get_second_order_neighbors(G, i)
    end = time.time()

    print(end - start)




