def cuttingRodRec(cost, length, w, n):
    if w == 0 or n == 0:
        return 0
    elif length[n - 1] > w:
        return cuttingRod(cost, length, w, n - 1)
    else:
        return max(
            cost[n - 1] + cuttingRod(cost, length, w - length[n - 1], n),
            cuttingRod(cost, length, w, n - 1),
        )


def cuttingRodDP(cost, length, w, n):
    dp = [[-1 for i in range(w + 2)] for j in range(n + 2)]

    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, w + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if length[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(cost[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j])
    return dp[n][w]


if __name__ == "__main__":
    cost = [1, 5, 8, 9, 10, 17, 17, 20]
    length = list(range(1, len(cost) + 1))
    w = len(cost)
    n = len(cost)
    print(cuttingRodDP(cost, length, w, n))
