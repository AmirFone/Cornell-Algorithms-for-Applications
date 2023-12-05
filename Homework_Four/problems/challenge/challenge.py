def find_max_form(strs, m, n):
    def count_zeros_ones(s):
        """ Count the number of zeros and ones in the string """
        zeros = s.count('0')
        ones = len(s) - zeros
        return zeros, ones

    # Initialize a 3D dynamic programming array
    dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]

    for i in range(1, len(strs) + 1):
        zeros, ones = count_zeros_ones(strs[i - 1])
        for j in range(m + 1):
            for k in range(n + 1):
                # If the current string can be added to the subset
                if zeros <= j and ones <= k:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)
                else:
                    dp[i][j][k] = dp[i - 1][j][k]

    return dp[-1][m][n]