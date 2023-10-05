'''
Problem 3b

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n (see README). 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n log n) as described in the homework.
'''
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while (i <= self.size):
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while (i >= 1):
            s += self.tree[i]
            i -= i & -i
        return s

def number_of_large_inversions_3b(file, delta):
    with open(file, 'r') as f:
        data = f.readlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))

    sorted_arr = sorted([(num, i + 1) for i, num in enumerate(arr)], reverse=True)
    fenwick = BIT(n)
    count = 0
    for i, (num, original_idx) in enumerate(sorted_arr):
        # Count of numbers that are greater and positioned more than delta indices before.
        if original_idx - delta - 1 > 0:
            count += fenwick.query(original_idx - delta - 1)
        fenwick.update(original_idx, 1)
    return count
