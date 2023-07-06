#similar to 0 1 knapsack

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def countWaysToMakeChange(denominations, value) :
    
	# Your code goes here
    n = len(denominations)
    dp = [[-1 for j in range(value+1)]for i in range(n)]
    return helper(n-1,denominations,value,dp)
#recursion
# def helper(ind,arr,tar):
#     if ind==0:
#         if tar%arr[0]==0:
#             return 1
#         else:
#             return 0
#     notpick = helper(ind-1,arr,tar)
#     pick = 0
#     if arr[ind]<=tar:
#         pick = helper(ind,arr,tar-arr[ind])
#     return pick+notpick



#memoization
def helper(ind,arr,tar,dp):
    if ind==0:
        if tar%arr[0]==0:
            return 1
        else:
            return 0
    if dp[ind][tar]!=-1:
        return dp[ind][tar]
    notpick = helper(ind-1,arr,tar,dp)
    pick = 0
    if arr[ind]<=tar:
        pick = helper(ind,arr,tar-arr[ind],dp)
    dp[ind][tar] = pick+notpick
    return dp[ind][tar]





















#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))
