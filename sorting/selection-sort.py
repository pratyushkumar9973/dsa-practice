def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini_index]:
                mini_index = j
        arr[i], arr[mini_index] = arr[mini_index], arr[i]
    return arr
