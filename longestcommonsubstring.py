#Longest Common Substring
from os import *
from sys import *
from collections import *
from math import *

def lcs(str1, str2):
    # Write your code here.
    n = len(str1)
    m = len(str2)
    dp = [[-1 for j in range(m+1)] for i in range(n+1)]
    return helper(n,m,str1,str2,dp)
    pass
    
def helper(ind1,ind2,s,t,dp):
    ans = 0
    for i in range(ind1+1):
        dp[i][0]=0
    for i in range(ind2+1):
        dp[0][i]=0
        
    for i in range(1,ind1+1):
        for j in range(1,ind2+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
                ans = max(dp[i][j],ans)
            else:
                dp[i][j] =0
    return ans
