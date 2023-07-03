def canPartition(arr, n):
    # Write your code here.
    summ = sum(arr)
    if (summ%2!=0):
        return False
    else:
        k = summ//2
        n = len(arr)
        dp = [[False for i in range(k+1)]for j in range(n)]
        return helper(n,k,arr,dp)
    pass


#same code as before just need to check for even or odd as total sum
def helper(n,k,arr,dp):
    for i in range(n):
        dp[i][0] = True
    
    
    for ind in range(n):
        for target in range(k+1):
            notTaken = dp[ind-1][target]
            taken = False
            if arr[ind] <= target:
                taken = dp[ind-1][target-arr[ind]]
            dp[ind][target] = notTaken or taken
    
    return dp[ind][target]
