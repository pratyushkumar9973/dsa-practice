def find_prices(prices, budget):
    seen = {}
    for i, price in enumerate(prices):
        need = budget - price
        if need in seen:
            return [seen[need], i]
        seen[price] = i
    return None

print(find_prices([2, 7, 11, 15], 9))
