# given 2 integer, determin weather
# or not they differ by one bit
# link : https://www.youtube.com/watch?v=LqxtPV8xKeI&list=PLNmW52ef0uwvkul_e_wLD525jbTfMKLIJ&index=3


def grayNumber(a, b):
    x = a ^ b
    while x > 0:
        if x % 2 == 1 and x >> 1 > 0:
            return False
        x >>= 1
    return True


def main():
    a = int(input())
    b = int(input())
    print(grayNumber(a, b))


if __name__ == "__main__":
    main()
