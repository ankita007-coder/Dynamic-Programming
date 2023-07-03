#calculate the minimum absolute difference

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def minSubsetSumDifference(nums, n):

    k = sum(nums)
    n = len(nums)
    dp = [[False for i in range(k+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True


    for ind in range(n):
        for target in range(k+1):
            notTaken = dp[ind-1][target]
            taken = False
            if nums[ind] <= target:
                taken = dp[ind-1][target-nums[ind]]
            dp[ind][target] = notTaken or taken

    mini = int(1e9)
    for i in range(k//2+1):
        if dp[ind][i]==True:
            mini = min(mini,abs(i-(k-i)))

            
    return mini

    # Write your code here.
    # Return the minimum difference in the form of an integer.
    # k = sum(nums)
    # tot =k
    #     #print(tot)
    # #n = len(nums)
    # dp = [[False]*(k+1) for i in range(n)]
    # for i in range(n):
    #     dp[i][0] =True
    # if nums[0]<=k: dp[0][nums[0]]=True
    # for i in range(1,n):
    #     for j in range(1,k+1):
    #         notpick = dp[i-1][j]
    #         pick = False
    #         if nums[i]<=j: pick = dp[i-1][j-nums[i]]
    #         dp[i][j] = pick or notpick
        
    # mini = 1e9
    # for i in range(tot//2+1):
    #     if dp[n-1][i]== True:
    #         mini = min(mini,abs((k-i)-i))
    # return mini        

    










# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = minSubsetSumDifference(arr, N)
    stdout.write(str(ans) + "\n")
    tc -= 1
