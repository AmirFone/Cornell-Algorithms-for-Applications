# Problem 1b


def maxsum_tree(vertices, adjacency) -> int:
    dp=[0]*len(vertices)
    for i in range(len(vertices)):
        if i==0:
            dp[i]=vertices[i]
        elif i==1:
            dp[i]=max(vertices[i],vertices[i-1])
        else:
            dp[i]=max(dp[i-1],dp[i-2]+vertices[i])
    
    return dp[-1]
    

