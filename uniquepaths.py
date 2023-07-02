from os import *
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
	# Write your code here.
	dp = [[-1 for j in range(n)] for i in range(m)]
	return helper(m-1,n-1,dp)
	pass


#recursion
# def helper(i,j):
# 	if i==0 and j==0:
# 		return 1
# 	if i<0 or j<0:
# 		return 0
# 	up = helper(i-1,j)
# 	left = helper(i,j-1)
# 	return up+left

#memoization
# def helper(i,j,dp):
# 	if i==0 and j==0:
# 		return 1
# 	if i<0 or j<0:
# 		return 0
# 	if dp[i][j]!=-1:
# 		return dp[i][j]
# 	up = helper(i-1,j,dp)
# 	left = helper(i,j-1,dp)
# 	dp[i][j]= up+left
# 	#print(dp)
# 	return dp[i][j]

#tabulation
def helper(m,n,dp):
	
	for i in range(m+1):
		for j in range(n+1):
			if i==0 and j==0:
				dp[i][j]=1
				continue
			up= 0
			left = 0
			if i>0:
				up = dp[i-1][j]
			if j>0:
				left = dp[i][j-1]
			dp[i][j] = up+left
		#print(dp)
	return dp[m][n]
			

