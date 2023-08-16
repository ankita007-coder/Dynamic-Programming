#Frog Jump with k distances

from typing import *

def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    # Write your code here.
    dp = [-1]*(n+1)
    return helper(n-1,k,heights,dp)
    pass
#recursion
# def helper(ind,k,arr):
#     if ind==0:
#         return 0
#     mini = 2134678
#     for i in range(1,k+1):
#         if (ind-i)>=0:
#             steps = helper(ind-i,k,arr)+abs(arr[ind]-arr[ind-i])
#             mini = min(mini,steps)
#     return mini

#memoization
# def helper(ind,k,arr,dp):
#     if ind==0:
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     mini = 2134678
#     for i in range(1,k+1):
#         if (ind-i)>=0:
#             steps = helper(ind-i,k,arr,dp)+abs(arr[ind]-arr[ind-i])
#             mini = min(mini,steps)
#             dp[ind]=mini
#     return dp[ind]

#tabulation
def helper(ind,k,arr,dp):
    dp[0]=0
    
    for j in range(1,ind+1):
        mini = 2134678
        for i in range(1,k+1): 
            if (j-i)>=0:
                steps = dp[j-i]+abs(arr[j]-arr[j-i])
                mini = min(mini,steps)
        dp[j]=mini
    return dp[ind]
