#code is same as Partitions With Given Difference

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def targetSum(arr: List[int], target: int) -> int:
    total = sum(arr)
    if ((total-target)<0 or ((total-target)%2!=0)): 
        return 0
    return helper(arr,(total-target)//2)
    pass
def helper(num: List[int], tar: int) -> int:
    # Write your code here.
    dp = [[0 for j in range(tar+1)] for i in range(len(num))]
    n = len(num)
    if num[0]==0: dp[0][0]=2
    else: dp[0][0]=1
    if (num[0]!=0 and num[0]<=tar): dp[0][num[0]]=1

    
    for ind in range(1,n):
        for target in range(tar+1):
            notTaken = dp[ind-1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind-1][target-num[ind]]
            dp[ind][target] = (notTaken + taken)%(10**9+7)
    
    return dp[n-1][tar]


