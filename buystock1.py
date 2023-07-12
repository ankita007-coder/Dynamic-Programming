#Best Time to Buy and Sell Stock
from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    n = len(prices)
    mini = prices[0]
    maxi = 0
    for i in range(1,n):
        diff = prices[i]-mini
        maxi = max(diff,maxi)
        mini = min(prices[i],mini)
    return maxi
