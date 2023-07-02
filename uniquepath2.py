#unique path with obstacles

def mazeObstacles(n, m, mat):
    # Write your code here.
    
    dp = [[-1 for j in range(m)] for i in range(n)]
    return helper(n-1,m-1,mat,dp)
    # for i in range(n):
    #     for j in range(m):
    #         if i>0 and j>0 and mat[i][j]==-1: 
    #             dp[i][j]=0
    #             continue
    #         if i==0 and j==0: 
    #             dp[i][j]=1
    #             continue
            
    #         up,left = 0,0
    #         if i>0: up = dp[i-1][j]
    #         if j>0: left = dp[i][j-1]
            
    #         dp[i][j]=(up+left)%(10**9+7)
    
    # return dp[n-1][m-1]        

#recursion 
#almost same as unique paths just add one more condition
#if i>=0 and j>=0 and mat[i][j] ==-1:
#         return 0


#memoization
# def helper(i,j,mat,dp):
        
#     if i>=0 and j>=0 and mat[i][j] ==-1:
#         return 0
#     if i==0 and j==0:
#         return 1
#     if i<0 or j<0:
#         return 0
#     if dp[i][j]!=-1: 
#         return dp[i][j]
#     #print(dp)
#     up = helper(i-1,j,mat,dp)
#     left = helper(i,j-1,mat,dp)
#     dp[i][j] = up+left
#     return dp[i][j]

#tabulation
def helper(i,j,mat,dp):

    dp[0][0] = 1
    for ii in range(i+1):
        for jj in range(j+1):
            if ii>=0 and jj>=0 and mat[ii][jj]==-1:
                dp[ii][jj]=0
                continue
            if ii==0 and jj==0:
                dp[ii][jj]=1
                continue
            up = 0
            left = 0

            if ii>0: up = dp[ii-1][jj]
            if jj>0: left = dp[ii][jj-1]
            dp[ii][jj] = (up+left)%(10**9+7)
    return dp[ii][jj]


