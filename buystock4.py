from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(arr, n, k):
    # Write your code here.
    dp = [[[0 for k in range(k+1)] for i in range(2)] for j in range(n+1)]
    #return helper(prices,0,n,1,2,dp)
    for ind in range(n-1,-1,-1):
        for buy in range(0,2):
            for cap in range(1,k+1):
                if(buy):
                    profit= max(-arr[ind]+dp[ind+1][0][cap],dp[ind+1][1][cap])
                else:
                    profit= max(dp[ind+1][0][cap],arr[ind]+dp[ind+1][1][cap-1])
                dp[ind][buy][cap] = profit
    return dp[0][1][k]
    pass
