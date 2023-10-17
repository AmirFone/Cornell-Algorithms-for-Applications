import math

def brute_force(xs):
    from itertools import combinations
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
    total = sum(xs)
    n = len(xs)
    dp = [[0 for i in range(total + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, total + 1): 
        dp[0][i]= False
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            dp[i][j] = dp[i - 1][j]
            if xs[i-1] <= j:
                dp[i][j] |= dp[i - 1][j - xs[i-1]]

    # Find the value closest to total//2
    for i in range(total//2, -1, -1):
        if dp[n][i]:
            min_diff = i
            break

    # Backtracking
    subset1 = []
    i, j = n, min_diff
    while(i > 0 and j >= 0):
        if dp[i - 1][j] == 0:
            subset1.append(i - 1)
            j -= xs[i - 1]
        i -= 1
    mask = [1 if i in subset1 else 0 for i in range(n)]
    return mask