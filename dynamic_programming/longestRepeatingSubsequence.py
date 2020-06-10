def longestRepeatingSubsequenceSupport(a, b, x, y):

    if x == 0 or y == 0:
        return 0
    elif a[x - 1] == b[y - 1] and x != y:
        return 1 + longestRepeatingSubsequenceSupport(a, b, x - 1, y - 1)
    else:
        return max(
            longestRepeatingSubsequenceSupport(a, b, x - 1, y),
            longestRepeatingSubsequenceSupport(a, b, x, y - 1),
        )


def longestRepeatingSubsequenceSupportDp(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            # only diff from lcs ,
            elif a[i - 1] == b[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[x][y]


def longestRepeatingSubsequence(a):
    print(longestRepeatingSubsequenceSupport(a, a, len(a), len(a)))
    print(longestRepeatingSubsequenceSupportDp(a, a, len(a), len(a)))


def main():
    s = input()
    longestRepeatingSubsequence(s)


if __name__ == "__main__":
    main()
