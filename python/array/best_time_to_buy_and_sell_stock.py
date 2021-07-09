def best_time(prices):
    left, right = 0, 1
    max_profit = 0

    while right < len(prices):
        # Is this profitable?
        if prices[right] > prices[left]:
            max_profit = max(max_profit, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
#prices = [7, 6, 4, 3, 1]
print(best_time(prices))
