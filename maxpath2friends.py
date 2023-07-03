#3-d DP : Ninja and his friends (DP-13)
#1463. Cherry Pickup II

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[-1 for k in range(m)] for j in range(m)] for i in range(n)]
        return self.helper(m,n,grid,dp)
    
    # #recursion
    # def helper(self,i,j1,j2,m,n,mat):
    #     if j1<0 or j2<0 or j1>=m or j2>=m:
    #         return 0
    #     if i==n-1:
    #         if j1==j2:
    #             return mat[i][j1]
    #         else:
    #             return  mat[i][j1] + mat[i][j2]
    #     maxi = int(-1e8)
    #     for d1 in range(-1,2):
    #         for d2 in range(-1,2):
    #             value = 0
    #             if j1==j2:
    #                 value = mat[i][j1]
    #             else:
    #                 value = mat[i][j1] + mat[i][j2]
    #             value += self.helper(i+1, d1+j1, d2+j2, m,n, mat)
    #             maxi = max(maxi,value)
    #     return maxi

    #memoization
    # def helper(self,i,j1,j2,m,n,mat,dp):
    #     if j1<0 or j2<0 or j1>=m or j2>=m:
    #         return 0
    #     if i==n-1:
    #         if j1==j2:
    #             return mat[i][j1]
    #         else:
    #             return  mat[i][j1] + mat[i][j2]
    #     if dp[i][j1][j2]!=-1:
    #         return dp[i][j1][j2]
    #     maxi = int(-1e8)
    #     for d1 in range(-1,2):
    #         for d2 in range(-1,2):
    #             value = 0
    #             if j1==j2:
    #                 value = mat[i][j1]
    #             else:
    #                 value = mat[i][j1] + mat[i][j2]
    #             value += self.helper(i+1, d1+j1, d2+j2, m,n, mat,dp)
    #             maxi = max(maxi,value)
    #     dp[i][j1][j2] = maxi
    #     return dp[i][j1][j2]


    #tabulation
    def helper(self,m,n,mat,dp):
        for j1 in range(m):
            for j2 in range(m):
                if j1==j2:
                    dp[n-1][j1][j2] = mat[n-1][j1]
                else:
                    dp[n-1][j1][j2] = mat[n-1][j1] + mat[n-1][j2]
        
        for i in range(n-2,-1,-1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = int(-1e9)
                    for d1 in range(-1,2):
                        for d2 in range(-1,2):
                            value = 0
                            if j1==j2:
                                value = mat[i][j1]
                            else:
                                value = mat[i][j1]+mat[i][j2]
                            if d1+j1>=0 and d1+j1<m and j2+d2>=0 and j2+d2<m:
                                value += dp[i+1][d1+j1][j2+d2]
                            else:
                                value += int(-1e8)
                            maxi = max(maxi,value)
                    dp[i][j1][j2] = maxi
        return dp[0][0][m-1]

    
