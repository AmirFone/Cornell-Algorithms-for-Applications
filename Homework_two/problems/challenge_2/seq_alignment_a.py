'''
Challenge 2a
'''

def sequence_align(x, y, c, delta):
    n = len(x)
    m = len(y)
    score = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        score[i][0] = i * delta
    for j in range(m+1):
        score[0][j] = j * delta
    for i in range(1, n+1):
        for j in range(1, m+1):
            score[i][j] = min(
                score[i-1][j-1] + c(x[i-1], y[j-1]),
                score[i-1][j] + delta,
                score[i][j-1] + delta)
    alignment = []
    i, j = n, m
    while i > 0 and j > 0:
        if score[i][j] == score[i-1][j-1] + c(x[i-1], y[j-1]):
            alignment.append((i,j))
            i -= 1
            j -= 1
        elif score[i][j] == score[i-1][j] + delta:
            i -= 1
        else:
            j -= 1
    alignment.reverse()
    return (alignment, score[n][m])
