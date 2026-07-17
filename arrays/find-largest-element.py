def find_largest(arr):  
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
    return largest

arr =[23, 45, 24, 31, 41, 43]
print(find_largest(arr))
