def find_factors(nums):
    result = []
    for i in range(1, nums + 1):
        if nums % i == 0:
            factors.append(i)
    return result
