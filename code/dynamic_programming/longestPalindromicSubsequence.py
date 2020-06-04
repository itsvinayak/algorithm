def lcsRec(a, b, x, y):
    if x == 0 or y == 0:
        return 0
    elif a[x - 1] == b[y - 1]:
        return 1 + lcsRec(a, b, x - 1, y - 1)
    else:
        return max(lcsRec(a, b, x - 1, y), lcsRec(a, b, x, y - 1))


def lcsDp(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(y + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[x][y]


def LongestPalindromicSubsequence(string):
    # string , rev_string
    return lcsDp(string, string[::-1], len(string), len(string))


def main():
    string = input()
    print(LongestPalindromicSubsequence(string))


if __name__ == "__main__":
    main()
