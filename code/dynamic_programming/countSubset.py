def countSubset(arr, n, k):
    dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, k + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]

    return dp[n][k]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    k = 5
    n = len(arr)

    print(countSubset(arr, n, k))
