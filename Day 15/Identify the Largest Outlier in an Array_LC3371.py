from collections import defaultdict
from typing import List

def getLargestOutlier(nums: List[int]) -> int:
    maxi = float("-inf")
    mapp = defaultdict(int)
    summ = 0
    for a in nums:
        mapp[a] += 1
        summ += a
    for a in nums:
        mapp[a] -= 1
        summ -= a
        if summ % 2 == 0:
            comp = summ // 2
            if mapp[comp] > 0:
                maxi = max(maxi , a)
        summ += a
        mapp[a] += 1
    return maxi