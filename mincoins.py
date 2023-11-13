def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
target_value = 11

result = min_coins(coins, target_value)
if result != -1:
    print(f"Minimum coins needed for {target_value}: {result}")
else:
    print(f"Cannot make {target_value} with the given coins.")
