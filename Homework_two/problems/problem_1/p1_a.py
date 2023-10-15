# Problem 1a

def maxsum_list(xs) -> int:
    dp=[0]*len(xs)    
    for i in range(len(xs)):
        if i==0:
            dp[i]=xs[i]
        elif i==1:
            dp[i]=max(xs[i],xs[i-1])
        else:
            dp[i]=max(dp[i-1],dp[i-2]+xs[i])
            
    return dp[-1] 
