'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''
def stable_matching_1c(file) -> dict:
    '''
    Computes a stable matching between doctors and hospitals using the Gale-Shapley algorithm.

    Args:
        file (str): Path to input file containing doctor and hospital preferences.

    Returns:
        dict: Dictionary mapping doctor IDs to assigned hospital IDs in the stable matching.

    Time Complexity: O(n^2) 
    Space Complexity: O(n)
    '''
    n = 0

    # Initialize empty preference lists
    hospitals_pref = []
    doctors_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])

    # Initialize proposals and pairs
    proposals = [0] * n
    pairs = [-1] * n
    free_hospitals = list(range(n))

    while free_hospitals:
        h = free_hospitals[0]
        d = hospitals_pref[h][proposals[h]]

        if pairs[d] == -1:
            pairs[d] = h
            free_hospitals.pop(0)
        else:
            h_prime = pairs[d]

            # Lookup hospital's rank in doctor's preference
            if doctors_pref[d].index(h) < doctors_pref[d].index(h_prime):
                pairs[d] = h
                free_hospitals.pop(0)
                free_hospitals.insert(0, h_prime)

        proposals[h] += 1

    return {d: h for d, h in enumerate(pairs)}