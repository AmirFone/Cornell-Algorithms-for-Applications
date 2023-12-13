def hash_functions(x, a, b, p, w):
    return [((a[i] * x + b[i]) % p) % w for i in range(len(a))]

# Implementing the count_min_sketch function
def count_min_sketch(a, b, w, p, stream):
    # Initializing the sketch matrix with zeros
    sketch_matrix = [[0 for _ in range(w)] for _ in range(len(a))]    
    # Process the stream of data
    for x in stream:
        # Calculate the hash values for this element
        hashes = hash_functions(x, a, b, p, w)
        for i, hash_value in enumerate(hashes):
            sketch_matrix[i][hash_value] += 1
            
    return sketch_matrix

# Parameters for the example
# a = [1, 2]
# b = [3, 5]
# w = 3
# p = 100

