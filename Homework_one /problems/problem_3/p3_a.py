'''
Problem 3a

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n (see README). 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n^2) as described in the homework.
'''
def number_of_large_inversions_3a(file, delta):
    with open(file, 'r') as f:
        data = f.readlines()
    n = int(data[0])
    ordering = list(map(int, data[1].split()))

    count = 0
    for i in range(len(ordering)):
        for j in range(i+1, len(ordering)):
            if ordering[i] > ordering[j] and (j-i) > delta: count += 1
    return count