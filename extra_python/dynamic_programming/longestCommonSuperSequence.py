def lcs(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[x][y]


def LongestCommonSequenceRec(a, b, x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    if a[x - 1] == b[y - 1]:
        return 1 + LongestCommonSequenceRec(a, b, x - 1, y - 1)
    else:
        return 1 + min(
            LongestCommonSequenceRec(a, b, x - 1, y),
            LongestCommonSequenceRec(a, b, x, y - 1),
        )


def LongestCommonSequenceDp(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[x][y]


def LongestCommonSequence(a, b, x, y):
    return x + y - lcs(a, b, x, y)


def PrintLongestCommonSequence(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    i = x
    j = y
    string = []
    while i > 0 and j > 0:

        if a[i - 1] == b[j - 1]:
            string.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            string.append(b[j - 1])
            j -= 1
        else:
            string.append(a[i - 1])
            i -= 1
    while i > 0:
        string.append(a[i - 1])
        i -= 1
    while j > 0:
        string.append(b[j - 1])
        j -= 1

    string.reverse()
    return "".join(string)


if __name__ == "__main__":
    a = input()
    b = input()
    x = len(a)
    y = len(b)

    print(LongestCommonSequenceRec(a, b, x, y))
    print(LongestCommonSequenceDp(a, b, x, y))
    print(LongestCommonSequence(a, b, x, y))
    print(PrintLongestCommonSequence(a, b, x, y))
