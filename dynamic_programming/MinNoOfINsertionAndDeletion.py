def MinNumberInsertionAndDel(a, b, x, y):
    dp = [[None for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[x][y]

    return (len(a) - lcs) + (len(b) - lcs)


def main():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        a, b = map(str, input().split())
        print(MinNumberInsertionAndDel(a, b, x, y))


if __name__ == "__main__":
    main()
