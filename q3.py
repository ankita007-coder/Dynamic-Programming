from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
# def helper(ind,nums):
#     if ind==0:
#         return nums[ind]
#     if ind<0:
#         return 0
    
#     pick = nums[0]
#     pick = helper(ind-2, nums)+nums[ind]
#     notpick = helper(ind-1,nums)
#     return max(pick,notpick)

#memoization
# def helper(ind,nums,dp):
#     if ind==0:
#         return nums[ind]
#     if ind<0:
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     pick = nums[0]
#     pick = helper(ind-2, nums,dp)+nums[ind]
#     notpick = helper(ind-1,nums,dp)
#     dp[ind] = max(pick,notpick)   
#     return dp[ind]

#tabulation
def helper(ind,nums,dp):
    dp[0] = nums[0]
    
    for i in range(1,ind+1):      
        pick = dp[i-2]+nums[i]
        notpick = dp[i-1]
        dp[i] = max(pick,notpick) 
    return dp[ind]      


def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp = [0]*(len(nums))
    return helper(len(nums)-1,nums,dp)
    # prev= nums[0]
    # prev2 = 0
    # for i in range(1,len(nums)):
    #     pick = nums[i]
    #     if i>1:
    #         pick+=prev2
    #     notpick = prev
    #     curr = max(pick,notpick)
    #     prev2,prev = prev,curr
    # return prev
    pass

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
