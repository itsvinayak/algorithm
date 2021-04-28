memo = []


def lcsRec(a, b, x, y):
    if x == 0 or y == 0:
        return 0
    elif a[x - 1] == b[y - 1]:
        return 1 + lcsRec(a, b, x - 1, y - 1)
    else:
        return max(lcsRec(a, b, x - 1, y), lcsRec(a, b, x, y - 1))


def lcsMemo(a, b, x, y):
    if x == 0 or y == 0:
        return 0
    elif memo[x - 1][y - 1] != None:
        return memo[x - 1][y - 1]
    elif a[x - 1] == b[y - 1]:
        memo[x - 1][y - 1] = 1 + lcsMemo(a, b, x - 1, y - 1)
        return memo[x - 1][y - 1]
    else:
        memo[x - 1][y - 1] = max(lcsMemo(a, b, x - 1, y), lcsMemo(a, b, x, y - 1))
        return memo[x - 1][y - 1]


def lcsDp(a, b, x, y):
    dp = [[None for i in range(y + 1)] for j in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[x][y]


def PrintLCS(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i = x
    j = y
    index = dp[x][y]
    string = [""] * (index + 1)
    string[index] = ""
    while i > 0 and j > 0:

        if a[i - 1] == b[j - 1]:
            string[index - 1] = a[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(string)


if __name__ == "__main__":
    a = input()
    b = input()
    memo = [[None for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
    print(lcsRec(a, b, len(a), len(b)))
    print(lcsMemo(a, b, len(a), len(b)))
    print(lcsDp(a, b, len(a), len(b)))
    print(PrintLCS(a, b, len(a), len(b)))
