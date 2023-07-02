# calculate minimum sum of the path

from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def minSumPath(grid):
    # Write your code here.
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for j in range(m)] for i in range(n)]
    return helper(n-1,m-1,grid,dp)
   
    pass

#memoization
# def helper(i,j,mat,dp):
        
#     if i==0 and j==0:
#         return mat[0][0]
#     if i<0 or j<0:
#         return 1e9
#     if dp[i][j]!=-1: 
#         return dp[i][j]
#     #print(dp)
#     up = mat[i][j]+ helper(i-1,j,mat,dp)
#     left = mat[i][j]+helper(i,j-1,mat,dp)
#     dp[i][j] = min(up,left)
#     return dp[i][j]


#tabulation

def helper(n,m,mat,dp):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0:
                dp[i][j] = mat[i][j]
            else:
                if i>0: 
                    up = dp[i-1][j]+mat[i][j]
                else:
                    up = 1e9
                if j>0: 
                    left = dp[i][j-1]+mat[i][j]
                else:
                    left = 1e9
                dp[i][j] = min(up,left)
        #print(dp)
    return dp[i][j]

# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1
