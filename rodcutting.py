from sys import stdin
import sys


def helper(ind,price,dp,N):
    
    for i in range(0,N+1):
        dp[0][i] = i*price[0]


    for i in range(1,ind+1):
        for j in range(N+1):

            pick = int(-1e9)
            notpick = dp[i-1][j]
            rodlen = i+1
            if rodlen<=j:
                pick = price[i]+dp[i][j-rodlen]
            
            dp[i][j]=max(pick,notpick)
    return dp[ind][N]

def cutRod(price, n):

    dp = [[0 for j in range(n+1)] for i in range(n) ]
    return helper(n-1,price,dp,n)

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
