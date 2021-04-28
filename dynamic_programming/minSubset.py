def minSubset(arr, n):
    k = sum(arr)
    dp = [[-1 for i in range(k + 2)] for j in range(n + 2)]

    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, k + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    l = dp[n][0 : (k // 2) + 1]
    ans = 999999999999999999
    for i in range(len(l)):
        if l[i]:
            ans = min(ans, k - 2 * i)
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        minSubset(arr, n)
