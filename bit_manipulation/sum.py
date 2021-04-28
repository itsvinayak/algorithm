# find sum of integer using bit manipulation
# link: https://www.youtube.com/watch?v=te4q1ivGons&list=PLNmW52ef0uwvkul_e_wLD525jbTfMKLIJ&index=5


def add(a, b):
    if b == 0:
        return a
    sum = a ^ b
    carray = (a & b) << 1
    print(bin(sum), " - ", bin(carray))
    return add(sum, carray)


def main():
    a, b = map(int, input().split())
    print(add(a, b))


if __name__ == "__main__":
    main()
