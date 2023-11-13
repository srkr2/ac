def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(1, n + 1):
        for w in range(capacity, 0, -1):
            if weights[i - 1] <= w:
                dp[w] = max(values[i - 1] + dp[w - weights[i - 1]], dp[w])

    return dp[capacity]

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = knapsack_01(values, weights, capacity)

print(f"Maximum value in the knapsack: {result}")
