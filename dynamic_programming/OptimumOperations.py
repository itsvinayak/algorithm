memo = [""] * 100000


def OptimumOperationRec(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 1 + OptimumOperationRec(n // 2)
    else:
        return 1 + OptimumOperationRec(n - 1)


def OptimumOperationMemo(n):
    if n == 0:
        return 0
    elif memo[n - 1] != "":
        return memo[n - 1]
    elif n % 2 == 0:
        memo[n - 1] = 1 + OptimumOperationMemo(n // 2)
        return memo[n - 1]
    else:
        memo[n - 1] = 1 + OptimumOperationMemo(n - 1)
        return memo[n - 1]


if __name__ == "__main__":
    n = int(input())
    print(OptimumOperationRec(n))
    print(OptimumOperationMemo(n))
