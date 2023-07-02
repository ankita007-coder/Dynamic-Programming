#calculating minimum path sum in triangular matrix

from os import *
from sys import *
from collections import *
from math import *

def minimumPathSum(triangle, n):
    # Write your code here.
    dp = [[-1 for i in range(n)] for j in range(n)]
    return helper(triangle,n,dp)
    # forward = triangle[n-1]
    #     #print(forward)
    # curr = [0]*n
    # for i in range(n-2,-1,-1):
    #     for j in range(i,-1,-1):
    #         down = forward[j]+triangle[i][j]
    #         dg = forward[j+1]+triangle[i][j]
            
    #         curr[j] = min(down,dg)
    #     forward = curr
    # return forward[0]




#recursion
# def helper(mat,i,j,n):
#     if i==n-1:
#         return mat[i][j]
#     down= mat[i][j]+helper(mat,i+1,j,n)
#     diag = mat[i][j]+helper(mat,i+1,j+1,n)
#     return min(down,diag)

#memoization
# def helper(mat,i,j,n,dp):
#     if i==n-1:
#         return mat[i][j]
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     down= mat[i][j]+helper(mat,i+1,j,n,dp)
#     diag = mat[i][j]+helper(mat,i+1,j+1,n,dp)
#     dp[i][j] = min(down,diag)
#     return dp[i][j]

#tabulation

def helper(mat,n,dp):
    for j in range(n):
        dp[n-1][j] = mat[n-1][j]   
    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            
            down= mat[i][j]+ dp[i+1][j]
            diag = mat[i][j]+dp[i+1][j+1]
            dp[i][j] = min(down,diag)
    #print(dp)
    return dp[0][0]



