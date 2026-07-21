def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    n,m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i < n:
        while i< n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(left[j])
            j += 1
    return result



arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))

