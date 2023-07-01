from os import *
from sys import *
from collections import *
from math import *

from typing import *
  
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [0]*(n)
    return helper(n,heights,dp)
    pass
    # prev,prev2 = 0,0
    
    # for i in range(1,len(heights)):
    #     ss = 214743678
    #     fs = prev+ abs(heights[i]-heights[i-1])
        
    #     if i>1:
    #         ss = prev2+ abs(heights[i]-heights[i-2])
    #     curr = min(fs,ss)
    #     prev2= prev
    #     prev = curr
    #return prev
    
# def helper(ind,h,dp):
#     if ind<=0:
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     twostep = 214743678
#     onestep = helper(ind-1,h,dp)+ abs(h[ind]-h[ind-1])
#     if ind>1:
#         twostep = helper(ind-2,h,dp)+abs(h[ind]-h[ind-2])
#     dp[ind] = min(onestep,twostep)
#     return dp[ind]

def helper(ind,h,dp):
    if ind==0:
        return 0
    twostep = 214743678 
    dp[0]=0 
    for i in range(1,ind):
        onestep = dp[i-1]+abs(h[i]-h[i-1])
        if i>1:
            twostep = dp[i-2]+abs(h[i]-h[i-2])
        dp[i] = min(onestep,twostep)
    return dp[ind-1]

