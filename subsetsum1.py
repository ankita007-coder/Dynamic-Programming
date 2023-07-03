from os import *
from sys import *
from collections import *
from math import *
#def f(n,k,arr):
    
def subsetSumToK(n, k, arr):

    # Write your code here
    dp = [[False for i in range(k+1)]for j in range(n)]
    return helper(n-1,k,arr,dp)
    # Return a boolean variable 'True' or 'False' denoting the answer
    # prev = [False]*(k+1)
    # prev[0]=True
    # if arr[0]<=k: 
    #     prev[arr[0]]=True
    # for i in range(1,n):
    #     curr = [False]*(k+1)
    #     curr[0]=True
    #     for j in range(1,k+1):
    #         notpick = prev[j]
    #         pick = False
    #         if arr[i]<=j:
    #             pick = prev[j-arr[i]]
    #         curr[j] = pick or notpick
    #     prev = curr
            
    # return prev[k]
#memoization
# def helper(n,k,arr,dp):
#     if k==0:
#         return True
#     if n==0:
#         return k==arr[0]
#     if dp[n][k]!=-1:
#         return dp[n][k]
#     notpick = helper(n-1,k,arr,dp)
#     pick = False
#     if arr[n]<=k:
#         pick = helper(n-1,k-arr[n],arr,dp)
    
#     dp[n][k] = pick or notpick
#     return dp[n][k]

#tabulation
def helper(n,k,arr,dp):
    for i in range(n):
        dp[i][0] = True
    
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for ind in range(1, n):
        for target in range(1, k+1):
            notTaken = dp[ind-1][target]
            taken = False
            if arr[ind] <= target:
                taken = dp[ind-1][target-arr[ind]]
            dp[ind][target] = notTaken or taken
    
    return dp[n-1][k]
    
    
    

