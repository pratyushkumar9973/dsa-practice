def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}
    
    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count

if __name__ == "__main__":
    print(subarraySum([1, 1, 1], 2))
    print(subarraySum([1, 2, 3], 3))
    print(subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))
