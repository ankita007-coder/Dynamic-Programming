#Minimum insertions to make a string palindrome


from os import *
from sys import *
from collections import *
from math import *

def longestPalindromeSubseq(s):
    t = s[::-1]
    m = len(s)
    dp = [[-1]*(m+1) for i in range(m+2)]
    for i in range(m+1):
        dp[i][0]=0
        dp[0][i]=0
    for i in range(1,m+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j],dp[i][j-1])
    return dp[m][m]
def minInsertion(s):
    # Write the function here.
    return len(s) - longestPalindromeSubseq(s)
