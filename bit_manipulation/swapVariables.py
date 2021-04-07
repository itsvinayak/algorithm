# given two integer swap them without using any temporary variable
# link : https://www.youtube.com/watch?v=DtnH3V_Vjek&list=PLNmW52ef0uwvkul_e_wLD525jbTfMKLIJ&index=4

# x = x + y
# y = x - y
# x = x - y


def swapVariables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return [a, b]


def main():
    a, b = map(int, input().split())
    print(*swapVariables(a, b))


if __name__ == "__main__":
    main()
