import math


def bits_per_link(csr_matrix):
    bits = 0
    rows, cols = csr_matrix.nonzero()
    for i in range(len(rows)):
        difference = rows[i] - cols[i]
        if difference != 0:
            bits += math.log2(abs(difference))
    
    bits_per_link = bits / len(rows)
    return bits_per_link