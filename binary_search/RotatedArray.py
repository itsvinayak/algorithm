def findRotatedarrayrray(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        if array[low] <= array[high]:
            return low

        mid = (low + high) // 2

        if (
            array[mid] <= array[(mid + 1) % len(array)]
            and array[mid] <= array[(mid - 1 + len(array)) % len(array)]
        ):
            return mid
        elif array[mid] <= array[high]:
            high = mid - 1
        elif array[mid] >= array[low]:
            low = mid + 1

    return -1


def main():
    array = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    print(findRotatedarrayrray(array))


if __name__ == "__main__":
    main()
