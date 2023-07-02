#Maximum Path Sum in the matrix


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getMaxPathSum(matrix):

    #   Write your code here
    n = len(matrix)
    m = len(matrix[0])
    maxi = int(-1e9)
    dp = [[-1 for j in range(m)]for i in range(n)]
    for j in range(m):
        maxi = max(maxi, helper(matrix,n-1,j,m,dp))
    return maxi
    pass

#recursion
# def helper(mat,i,j,m):
#     if j<0 or j>=m:
#         return int(-1e9)
#     if i==0:
#         return mat[0][j]
#     up = mat[i][j] + helper(mat,i-1,j,m)
#     left = mat[i][j] + helper(mat,i-1,j-1,m)
#     right = mat[i][j] + helper(mat,i-1,j+1,m)
#     return max(up,left,right)

#memoization
# def helper(mat,i,j,m,dp):
#     if j<0 or j>=m:
#         return int(-1e9)
#     if i==0:
#         return mat[0][j]
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     up = mat[i][j] + helper(mat,i-1,j,m,dp)
#     left = mat[i][j] + helper(mat,i-1,j-1,m,dp)
#     right = mat[i][j] + helper(mat,i-1,j+1,m,dp)
#     dp[i][j]=max(up,left,right)
#     return dp[i][j]

#tabulation
def helper(mat,i,j,m,dp):
    
    if i==0:
        return mat[0][j]
    for r in range(i+1):
        for c in range(j+1):
            if r==0:
                dp[r][c]= mat[0][c]
            else:
                up,left,right = int(-1e9),int(-1e9),int(-1e9)
                if r>0:
                    up = mat[r][c] + dp[r-1][c]
                if r>0 and c>0:
                    left = mat[r][c] + dp[r-1][c-1]
                if r>0 and c<m-1:
                    right = mat[r][c] + dp[r-1][c+1]
                dp[r][c]=max(up,left,right)
    return dp[i][j]





















#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
