def LCSRec(a, b, x, y, count):
    if x == 0 or y == 0:
        return 0
    if a[x - 1] == b[y - 1]:
        count = LCSRec(a, b, x - 1, y - 1, count + 1)
    count = max(count, max(LCSRec(a, b, x, y - 1, 0), LCSRec(a, b, x - 1, y, 0)))
    return count


def LCSDp(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]
    result = 0
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return dp[x][y]


if __name__ == "__main__":
    a, b = input().split()
    x, y = len(a), len(b)
    print(LCSRec(a, b, x, y, 0))
    print(LCSDp(a, b, x, y))
