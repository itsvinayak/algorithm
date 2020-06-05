import sys


memo = [[None for _ in range(1001)] for _ in range(1001)]


def MatrixChainMultiplicationRec(array, i, j):
    if i == j:
        return 0
    minn = sys.maxsize

    for k in range(i, j):
        count = (
            MatrixChainMultiplicationRec(array, i, k)
            + MatrixChainMultiplicationRec(array, k + 1, j)
            + (array[i - 1] * array[k] * array[j])
        )
        minn = min(minn, count)

    return minn


def MatrixChainMultiplicationMemo(array, i, j):
    if i == j:
        return 0
    if memo[i][j] is not None:
        return memo[i][j]

    minn = sys.maxsize

    for k in range(i, j):
        count = (
            MatrixChainMultiplicationMemo(array, i, k)
            + MatrixChainMultiplicationMemo(array, k + 1, j)
            + (array[i - 1] * array[k] * array[j])
        )
        minn = min(minn, count)
    memo[i][j] = minn
    return memo[i][j]


def MatrixChainMultiplicationDp(array, n):
    """ n is length of array """
    dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = sys.maxsize
                for k in range(i + 1, j):
                    count = (
                        dp[i][k] + dp[k + 1][j] + (array[i - 1] * array[k] * array[j])
                    )
                    dp[i][j] = min(count, dp[i][j])

    return dp[n][n]


def main():
    array = [1, 2, 3, 4, 3]
    print(MatrixChainMultiplicationRec(array, 1, len(array) - 1))
    print(MatrixChainMultiplicationMemo(array, 1, len(array) - 1))
    print(MatrixChainMultiplicationDp(array, len(array)))


if __name__ == "__main__":
    main()
