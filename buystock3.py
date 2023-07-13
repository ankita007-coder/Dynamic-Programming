from os import *
from sys import *
from collections import *
from math import *

def maxProfit(arr, n):

    # Write your code here.
    dp = [[[0 for k in range(3)] for i in range(2)] for j in range(n+1)]
    #return helper(prices,0,n,1,2,dp)
    for ind in range(n-1,-1,-1):
        for buy in range(0,2):
            for cap in range(1,3):
                if(buy):
                    profit= max(-arr[ind]+dp[ind+1][0][cap],dp[ind+1][1][cap])
                else:
                    profit= max(dp[ind+1][0][cap],arr[ind]+dp[ind+1][1][cap-1])
                dp[ind][buy][cap] = profit
    return dp[0][1][2]
    pass

# def helper(arr,ind,n,buy,cap,dp):
#     if cap==0: return 0
#     if ind==n: return 0

#     if dp[ind][buy][cap]!=-1:
#         return dp[ind][buy][cap]
    
#     if(buy):
#         profit= max(-arr[ind]+helper(arr,ind+1,n,0,cap,dp),helper(arr,ind+1,n,1,cap,dp))
#     else:
#         profit= max(helper(arr,ind+1,n,0,cap,dp),arr[ind]+helper(arr,ind+1,n,1,cap-1,dp))
#     dp[ind][buy][cap] = profit
#     return dp[ind][buy][cap]
    
#def helper(arr,n,dp):

