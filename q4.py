from os import *
from sys import *
from collections import *
from math import *
def helper(nums):
    prev = nums[0]
    prev2 = 0
    for i in range(1,len(nums)):
        pick = nums[i]
        if i>1:pick+= prev2
        notpick = prev
        curr = max(pick,notpick)
        prev2 = prev
        prev = curr
    return prev
def houseRobber(valueInHouse):
    # Write your function here.
    #tmp1,tmp2 = [],[]
    n = len(valueInHouse)
    if n==1:
        return valueInHouse[0]    
    return max(helper(valueInHouse[1:]),helper(valueInHouse[0:n-1]))
    
    
