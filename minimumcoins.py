#We are given a target sum of ‘X’ and ‘N’ distinct numbers denoting the coin denominations.
#We need to tell the minimum number of coins required to reach the target sum. We can pick a coin denomination for any number of times we want.


from os import *
from sys import *
from collections import *
from math import *

from typing import List

def minimumElements(arr: List[int], T: int) -> int:
    #Write your code here.
    #tabulation
    n = len(arr)
    dp = [[0 for j in range(T + 1)] for i in range(n)]

    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = i // arr[0]
        else:
            dp[0][i] = int(1e9)
    
    for ind in range(1, n):
        for target in range(T + 1):
            notTake = 0 + dp[ind - 1][target]
            take = int(1e9)
            if arr[ind] <= target:
                take = 1 + dp[ind][target - arr[ind]]
            dp[ind][target] = min(notTake, take)
    
    ans = dp[n - 1][T]
    if ans >= int(1e9):
        return -1
    return ans

#memoization    
# def helper(ind,tar,nums,dp):
#     if ind==0:
#         if tar%nums[ind]==0:
#             return tar//nums[ind]
#         else: return 1e9
#     if dp[ind][tar]!=-1:
#         return dp[ind][tar]
#     notpick = helper(ind-1,tar,nums,dp)
#     pick = 1e9
#     if nums[ind]<=tar:
#         pick = 1+helper(ind,tar-nums[ind],nums,dp)
#     dp[ind][tar]=min(pick,notpick)
#     return dp[ind][tar]
    
def helper(ind,tar,nums,dp):
    
    for i in range(tar+1):
        if i%nums[0]==0:
            dp[0][i]= i//nums[0]
        else:
            dp[0][i] = int(1e9)


    for i in range(1,ind+1):
        for j in range(tar+1):

            pick = int(1e9)
            notpick = dp[i-1][j]
            if nums[i]<=j:
                pick = 1+dp[i-1][j-nums[i]]
            
            dp[i][j]=min(pick,notpick)
    return dp[ind][tar]
