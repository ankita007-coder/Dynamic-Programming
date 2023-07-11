#Minimum Insertions/Deletions to Convert String to same string

from os import *
from sys import *
from collections import *
from math import *
def longestPalindromeSubseq(s,t):
    m = len(s)
    n = len(t)
    dp = [[-1]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        dp[i][0]=0
    for j in range(n+1):
        dp[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
def canYouMake(s: str, p: str) -> int:
    # Write your code here.
    common = longestPalindromeSubseq(s,p)
    n = len(s)-common
    m = len(p)-common
    return n+m
    pass
