def ones(x):
    ans = 0
    while x > 0:
        ans += x & 1
        x >>= 1
    return ans


def main():
    n = int(input())
    print(ones(n))


if __name__ == "__main__":
    main()
