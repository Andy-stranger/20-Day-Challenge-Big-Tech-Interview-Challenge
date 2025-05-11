def threeSum(nums):
    n = len(nums)
    res = set()
    for i in range(n):
        req = set()
        for ind in range(i+1,n):
            comp = -(nums[i] + nums[ind])
            if comp in req:
                triplet = tuple(sorted((nums[i],comp,nums[ind])))
                res.add(triplet)
            req.add(nums[ind])
    return [list(tr) for tr in res]