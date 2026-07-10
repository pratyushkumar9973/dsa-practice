def find_lonely(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    for num, times in count.items():
        if times == 1:
            return num
    return None

print(find_lonely([2, 3, 2, 4, 3]))
