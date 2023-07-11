#Longest Palindromic Subsequence

class Solution:
    # def helper(self,ind1,ind2,text1,text2,dp):
    #     if ind1<0 or ind2<0:
    #         return 0
    #     if dp[ind1][ind2]!=-1:
    #         return dp[ind1][ind2]
    #     if text1[ind1]==text2[ind2]:
    #         dp[ind1][ind2] = 1+self.helper(ind1-1,ind2-1,text1,text2,dp)
    #         return dp[ind1][ind2]
    #     else:
    #         dp[ind1][ind2] = max(self.helper(ind1-1,ind2,text1,text2,dp),self.helper(ind1,ind2-1,text1,text2,dp))
    #         return dp[ind1][ind2]
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        m = len(s)
        dp = [[-1]*(m+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0
        for i in range(1,m+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j],dp[i][j-1])
        return dp[m][m]
    
