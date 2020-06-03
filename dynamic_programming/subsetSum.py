no_of_rows = 8  # k+1
no_of_cols = 7  # n+1

memoizaion = [[-1 for _ in range(no_of_cols)] for _ in range(no_of_rows)]


def isSubsetSumRec(arr, n, k):
    if k == 0:
        return True
    elif k != 0 and n == 0:
        return False
    elif arr[n - 1] > k:
        return isSubsetSum(arr, n - 1, k)
    else:
        return isSubsetSum(arr, n - 1, k) or isSubsetSum(arr, n - 1, k - arr[n - 1])


def isSubsetSumMemo(arr, n, k):
    if k == 0:
        return True
    elif k != 0 and n == 0:
        return False
    elif memoization[n - 1][k - 1] != -1:
        return memoization[n - 1][k - 1]
    elif arr[n - 1] > k:
        memoization[n - 1][k - 1] = isSubsetSumMemo(arr, n - 1, k)
        return memoization[n - 1][k - 1]
    else:
        memoization[n - 1][k - 1] = isSubsetSumMemo(arr, n - 1, k) or isSubsetSumMemo(
            arr, n - 1, k - arr[n - 1]
        )
        return memoization[n - 1][k - 1]


def isSubsetSumDp(arr, n, k):
    dp = [[-1 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, k):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    return dp[n - 1][k - 1]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    k = 7
    n = len(arr)
    if isSubsetSumDp(arr, n, k) == True:
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")
