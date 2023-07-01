from os import *
from sys import *
from collections import *
from math import *

def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    dp = [-1]*(nStairs+1)
    return helper(nStairs, dp)
    pass
#recursion
# def helper(n):
#     if n==0 or n==1:
#         return 1
#     return helper(n-1)+helper(n-2)


#memoization
# def helper(n, dp):
#     if n==1 or n==0:
#         return 1
#     if dp[n]!=-1:
#         return dp[n]%(1000000007)
#     else:
#         dp[n] = helper(n-1,dp)+helper(n-2,dp)
#         return dp[n]%(1000000007)

#tabulation
def helper(n,dp):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    dp[0],dp[1],dp[2]=1,1,2
    for i in range(3,n+1):
        dp[i]= dp[i-1]+dp[i-2]
    return dp[n]%1000000007
