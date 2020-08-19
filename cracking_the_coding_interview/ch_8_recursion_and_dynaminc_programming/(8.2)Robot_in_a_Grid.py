def RobotInAGrid(m, n):
    if m == 1 or n == 1:
        return 1
    return RobotInAGrid(m - 1, n) + RobotInAGrid(m, n - 1)


def main():
    m, n = map(int, input().split())
    print(RobotInAGrid(m, n))


if __name__ == "__main__":
    main()
