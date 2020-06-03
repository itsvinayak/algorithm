def countSubsetSumRec(arr, n, k):
    if k == 0:
        return 1
    elif n == 0 and k != 0:
        return 0
    elif k < arr[n - 1]:
        return countSubsetSumRec(arr, n - 1, k)
    else:
        return countSubsetSumRec(arr, n - 1, k) + countSubsetSumRec(
            arr, n - 1, k - arr[n - 1]
        )


def countSubsetSum(arr, n, k):
    dp = [[-1 for i in range(k + 1)] for j in range(n + 1)]

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
    return dp[i][j]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    k = 7
    n = len(arr)

    print(countSubsetSum(arr, n, k))
