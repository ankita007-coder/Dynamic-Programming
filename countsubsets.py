#counting the number of subsets with sum k

# from os import *
# from sys import *
# from collections import *
# from math import *

# from typing import List

# def findWays(num: List[int], tar: int) -> int:
#     # Write your code here.
#     dp = [[-1 for j in range(tar+1)] for i in range(len(num))]
#     n = len(num)
#     for i in range(n):
#         dp[i][0] = 1
    
    
#     for ind in range(n):
#         for target in range(tar+1):
#             notTaken = dp[ind-1][target]
#             taken = 0
#             if num[ind] <= target:
#                 taken = dp[ind-1][target-num[ind]]
#             dp[ind][target] = notTaken + taken
    
#     return dp[n-1][tar]
#     pass
    
from os import *
from sys import *
from collections import *
from math import *

from typing import List

def findWays(num: List[int], tar: int) -> int:
    # Write your code here.
    n = len(num)
    prev = [0]*(tar+1)
    prev[0]=1
    #if tar==0: return 1
    if num[0]<=tar: prev[num[0]]=1
    for i in range(1,n):
        curr = [0]*(tar+1)
        curr[0]=1
        for j in range(0,tar+1):
            notpick = prev[j]
            pick = 0
            if num[i]<=j: 
                pick = prev[j-num[i]]
            curr[j] = pick+notpick
        prev = curr
    return prev[tar]

    pass
