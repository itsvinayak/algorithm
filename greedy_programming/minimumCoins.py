def minCoins(value, List, pos):
    if value == 0:
        return 0
    if List[pos] > value:
        return minCoins(value, List, pos - 1)

    return 1 + minCoins(value - List[pos], List, pos - 1)


def main():
    List = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    V = int(input())

    print(minCoins(V, List, len(List) - 1))


if __name__ == "__main__":
    main()
