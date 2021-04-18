def RotateBits(n, d):
    INT_BITS = 32
    return (n >> d) | (n << (INT_BITS - d))


def main():
    n, k = map(int, input().split())
    print(bin(n))
    ans = RotateBits(n, k)
    print(bin(ans))
    print(ans)


if __name__ == "__main__":
    main()
