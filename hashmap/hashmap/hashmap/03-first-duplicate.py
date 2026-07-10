def first_duplicate(word):
    seen = {}
    for i, letter in enumerate(word):
        if letter in seen:
            return letter
        seen[letter] = i
    return None

print(first_duplicate("hello"))
