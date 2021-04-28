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


def sequencePattenMaching(a, b):
    if lcs(a, b, len(a), len(b)) == min(len(a), len(b)):
        return True
    else:
        return False


def main():
    a = input()
    b = input()
    print(sequencePattenMaching(a, b))


if __name__ == "__main__":
    main()
