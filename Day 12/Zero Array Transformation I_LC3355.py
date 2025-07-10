from typing import List

def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    diff = [0]*(n+1)
    for s,e in queries:
        diff[s] += 1
        diff[e+1] -= 1
    for i in range(1,n):
        diff[i] += diff[i-1]
    for i in range(n):
        if diff[i] < nums[i]:
            return False
    return True