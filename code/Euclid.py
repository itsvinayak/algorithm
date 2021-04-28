def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def main():
    a = 19
    b = 20
    print(gcd(a, b))


if __name__ == "__main__":
    main()
