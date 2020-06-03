def fibRec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibRec(n - 1) + fibRec(n - 2)


def fibDp(n):
    dp = [None for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    n = int(input("Enter a no. : "))

    #     print(fibRec(n))
    print(fibDp(n))
