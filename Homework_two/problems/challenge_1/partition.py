import math
from itertools import combinations

def brute_force(xs):
    s = sum(xs)
    min_diff = float('inf')
    for i in range(1, len(xs) // 2 + 1):
        for combination in combinations(xs, i):
            diff = abs(s - 2 * sum(combination))
            if diff < min_diff:
                min_diff = diff
                min_combination = combination
    return [int(x in min_combination) for x in xs]

def greedy(xs):
    pass


def dp(xs):
    pass
