#Best Time to Buy and Sell Stock II

from sys import stdin


def getMaximumProfit(values, n) :
	#Your code goes here
    ans = 0
    for i in range(1,n):
        if values[i]>values[i-1]:
            ans+=(values[i]-values[i-1])
    return ans






























#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
