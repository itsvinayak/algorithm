no_of_cols = 4  # n+1
no_of_rows = 51  # W+1

memoization = [[-1 for i in range(no_of_cols)] for j in range(no_of_rows)]


def recursiveKnapsack(val, wt, W, n):
    if n == 0 or W == 0:
        return 0
    elif wt[n - 1] > W:
        return recursiveKnapsack(val, wt, W, n - 1)
    else:
        return max(
            val[n - 1] + recursiveKnapsack(val, wt, W - wt[n - 1], n - 1),
            recursiveKnapsack(val, wt, W, n - 1),
        )


def memoizationKnapsack(val, wt, W, n):
    if n == 0 or W == 0:
        return 0
    elif wt[n - 1] > W:
        memoization[W - 1][n - 1] = memoizationKnapsack(val, wt, W, n - 1)
        return memoization[W - 1][n - 1]
    elif memoization[W - 1][n - 1] != -1:
        return memoization[W - 1][n - 1]
    else:
        memoization[W - 1][n - 1] = max(
            val[n - 1] + memoizationKnapsack(val, wt, W - wt[n - 1], n - 1),
            memoizationKnapsack(val, wt, W, n - 1),
        )
        return memoization[W - 1][n - 1]


def topDownKnapsack(val, wt, W, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i - 1] <= W:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)

    print(recursiveKnapsack(val, wt, W, n))
    print(memoizationKnapsack(val, wt, W, n))
    print(topDownKnapsack(val, wt, W, n))
