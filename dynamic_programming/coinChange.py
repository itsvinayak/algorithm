def coinChangeRec(arr, k, n):
    if n == 0:
        return 0
    elif k == 0:
        return 1
    elif k < arr[n - 1]:
        return coinChangeRec(arr, k, n - 1)
    else:
        return coinChangeRec(arr, k, n - 1) + coinChangeRec(arr, k - arr[n - 1], n)


def coinChangeDp(arr, k, n):
    dp = [[-1 for i in range(k + 2)] for j in range(n + 2)]

    # base case init
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, k + 1):
        dp[0][i] = 0

    # rec call using arr
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - arr[i - 1]]
    return dp[n][k]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        print(coinChangeDp(arr, k, n))
