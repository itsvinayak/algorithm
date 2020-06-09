import sys


def MinCoinRec(arr, n, k):
    if k == 0:
        return 0

    ans = sys.maxsize
    for i in range(0, n):
        if arr[i] <= k:
            ans = min(ans, 1 + MinCoin(arr, n, k - arr[i]))
    return ans


def MinCoinDp(arr, n, k):
    dp = [[-1 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, k + 1):
        dp[0][i] = sys.maxsize

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if arr[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - arr[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][k]


if __name__ == "__main__":
    for _ in range(int(input())):
        k, n = map(int, input().split())
        arr = list(map(int, input().split()))
        print(MinCoinDp(arr, n, k))
