from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def helper(ind,wt,val,W,dp):
    
    for i in range(wt[0],W+1):
        dp[0][i] = val[0]


    for i in range(1,ind+1):
        for j in range(W+1):

            pick = int(-1e9)
            notpick = dp[i-1][j]
            if wt[i]<=j:
                pick = val[i]+dp[i-1][j-wt[i]]
            
            dp[i][j]=max(pick,notpick)
    return dp[ind][W]


def knapsack(n,wt,val,W):
    dp = [[0 for j in range(W+1)] for i in range(n) ]
    return helper(n-1,wt,val,W,dp)





t = int(input())
while t>0:
    n = int(input())
    wt = list(map(int,input().split()))
    val = list(map(int,input().split()))
    W = int(input())
    num = len(wt)
    print(knapsack(num,wt,val,W))
    t-=1
