def SubsetSum(arr, n, k):
    dp = [[-1 for i in range(k + 2)] for j in range(n + 2)]

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


def main():
    arr = [1, 1, 2, 3]
    to = 1

    k = to + sum(arr) // 2
    n = len(arr)
    print(SubsetSum(arr, n, k))


if __name__ == "__main__":
    main()
