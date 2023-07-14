from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumProfit(n: int, fee: int, prices: List[int]) -> int:
    # write your code here
    n = len(prices)
    dp = [[-1 for i in range(2)] for j in range(n)]
    return helper(prices,0,n,1,fee,dp)
    pass

def helper(arr,ind,n,buy,fee,dp):
    if ind>=n: return 0

    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    
    if(buy):
        profit= max(-arr[ind]+helper(arr,ind+1,n,0,fee,dp),
                    helper(arr,ind+1,n,1,fee,dp))
    else:
        profit= max(helper(arr,ind+1,n,0,fee,dp),
        arr[ind]-fee+helper(arr,ind+1,n,1,fee,dp))
    dp[ind][buy] = profit
    return dp[ind][buy]

