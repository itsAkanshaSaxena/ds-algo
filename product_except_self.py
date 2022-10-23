def solutions(nums):
    prod = 1
    res = []

    for i in range(len(nums)):
        res.append(prod)
        prod = prod * nums[i]

    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * prod
        prod = prod * nums[i]
    return res
