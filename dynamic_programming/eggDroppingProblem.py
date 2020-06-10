memo = [[None for _ in range(100)] for _ in range(100)]


def eggDroppingProblemRec(egg, floor):
    if egg == 1 or floor == 0 or floor == 1:
        return floor
    else:
        ans = float("inf")

        for k in range(1, floor + 1):
            temp = 1 + max(
                eggDroppingProblemRec(egg - 1, k - 1),
                eggDroppingProblemRec(egg, floor - k),
            )
            ans = min(ans, temp)
        return ans


def eggDroppingProblemDp(egg, floor):
    if egg == 1 or floor == 0 or floor == 1:
        return floor
    elif memo[egg][floor] is not None:
        return memo[egg][floor]
    else:
        ans = float("inf")

        for k in range(1, floor + 1):
            temp = 1 + max(
                eggDroppingProblemDp(egg - 1, k - 1),
                eggDroppingProblemDp(egg, floor - k),
            )
            ans = min(ans, temp)
        memo[egg][floor] = ans
        return memo[egg][floor]


def main():
    egg = 2
    floor = 10
    print(eggDroppingProblemRec(egg, floor))
    print(eggDroppingProblemDp(egg, floor))


if __name__ == "__main__":
    main()
