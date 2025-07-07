def numSubarrayProductLessThanK(self, nums, k):
    if k <= 1:
        return 0
    res = 0
    l = 0
    prd = 1
    for r in range(len(nums)):
        prd *= nums[r]
        while prd >= k:
            prd //= nums[l]
            l += 1
        res += r-l+1
    return res