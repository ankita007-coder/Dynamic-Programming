#Longest Common Subsequence
from sys import stdin

def lcs(s, t) :
	#Your code goes here
    ind1 = len(s)
    ind2 = len(t)
    dp = [[-1 for i in range(ind2+1)]for j in range(ind1+1)]
    # for i in range(ind1+1):
    #     dp[i][0]=0
    # for i in range(ind2+1):
    #     dp[0][i]=0
        
    # for i in range(1,ind1+1):
    #     for j in range(1,ind2+1):
    #         if s[i-1]==t[j-1]:
    #             dp[i][j] = 1+ dp[i-1][j-1]
    #         else:
    #             dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    # return dp[ind1][ind2]
    return helper(ind1-1,ind2-1,s,t,dp)
#memoization
# def helper(ind1,ind2,s,t,dp):
#     if ind1<0 or ind2<0:
#         return 0
#     if dp[ind1][ind2]!=-1:
#         return dp[ind1][ind2]
#     if s[ind1]==t[ind2]:
#         dp[ind1][ind2] = 1+ helper(ind1-1,ind2-1,s,t,dp)
#     else:
#         dp[ind1][ind2] = max(helper(ind1,ind2-1,s,t,dp),helper(ind1-1,ind2,s,t,dp))
#     return dp[ind1][ind2]
#tabulation
def helper(ind1,ind2,s,t,dp):
    for i in range(ind1+1):
        dp[i][0]=0
    for i in range(ind2+1):
        dp[0][i]=0
        
    for i in range(1,ind1+1):
        for j in range(1,ind2+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[ind1][ind2]























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))
