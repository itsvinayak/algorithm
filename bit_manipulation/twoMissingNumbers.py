def oneMissingNumbers(array):
    fullXor = 0
    orgXor = 0

    for i in range(1, len(array) + 2):
        fullXor ^= i

    for i in array:
        orgXor ^= i

    return abs(fullXor - orgXor)


def twoMissingNumbers(array):
    size = len(array) + 2
    totalsum = size * (size - 1) / 2
    arrSum = sum(array)
    pivot = (totalsum - arrSum) / 2


def main():
    array = [1, 2, 4, 5, 6]
    print(oneMissingNumbers(array))


if __name__ == "__main__":
    main()
