def binarySearch(array, find):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if find == array[mid]:
            print(*array, "  : element found at :", mid)
            break
        elif find > array[mid]:
            start = mid + 1
        else:
            end = mid - 1


def main():
    array = [1, 2, 3, 4, 8, 9, 10, 20, 21, 24, 30]
    find = 10
    binarySearch(array, find)


if __name__ == "__main__":
    main()
