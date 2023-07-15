from sys import stdin
import sys 
sys.setrecursionlimit(10**7)
def longestIncreasingSubsequence(arr, n) :

	# Your code goes here
   # dp = [[-1 for i in range(n+1)] for j in range(n)]
    #return helper(arr,0,-1,n,dp)
    #return helper(arr,n)

    tails = [0] * n
    size = 0
    for x in arr:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size




#memoization
# def helper(arr,ind,prev,n,dp):
#     if ind==n:
#         return 0
#     if dp[ind][prev]!=-1:
#         return dp[ind][prev]
#     take = -1e9
#     nottake = helper(arr,ind+1,prev,n,dp)
#     if prev==-1 or arr[ind]>arr[prev]:
#         take = 1+helper(arr,ind+1,ind,n,dp)
#     dp[ind][prev] = max(take,nottake)
#     return dp[ind][prev]

#tabulation

#def helper(arr,n):
    # Initialization
    

    # dp = [1 for i in range(n)]
    # for i in range(n-1,-1,-1):
    #     for j in range(i+1,n):
    #         if arr[i]<arr[j]:
    #             dp[i] = max(dp[i],1+dp[j])
    # return max(dp)






























#taking inpit using fast I/O
def takeInput() :
    n = int(input())

    if n==0 :
        return list(), n
        
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))
