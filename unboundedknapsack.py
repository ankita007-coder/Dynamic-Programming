
def helper(ind,wt,val,W,dp):
    
    for i in range(wt[0],W+1):
        dp[0][i] = val[0]*(i//wt[0])


    for i in range(1,ind+1):
        for j in range(W+1):

            pick = int(-1e9)
            notpick = dp[i-1][j]
            if wt[i]<=j:
                pick = val[i]+dp[i][j-wt[i]]
            
            dp[i][j]=max(pick,notpick)
    return dp[ind][W]


def unboundedKnapsack(n,W,val,wt):
    dp = [[0 for j in range(W+1)] for i in range(n) ]
    return helper(n-1,wt,val,W,dp)
