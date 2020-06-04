def recursiveUnboundedKnapsack(val, wt, W, n):
    if n == 0 or W == 0:
        return 0
    elif wt[n - 1] > W:
        return recursiveUnboundedKnapsack(val, wt, W, n - 1)
    else:
        return max(
            val[n - 1] + recursiveUnboundedKnapsack(val, wt, W - wt[n - 1], n),
            recursiveUnboundedKnapsack(val, wt, W, n - 1),
        )


def unboundedKnapsackDp(val, wt, W, n):
    dp = [[None for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or W == 0:
                return 0
            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
    return dp[n][W]


if __name__ == "__main__":
    val = [40, 60, 50]
    wt = [12, 20, 15]
    n = 3
    W = 45
    print(recursiveUnboundedKnapsack(val, wt, W, n))
    print(unboundedKnapsackDp(val, wt, W, n))
