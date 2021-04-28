def first(array, element):
    low = 0
    high = len(array) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] > element:
            high = mid - 1
        elif array[mid] < element:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans


def last(array, element):
    low = 0
    high = len(array) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] > element:
            high = mid - 1
        elif array[mid] < element:
            low = mid + 1
        else:
            ans = mid
            low = mid + 1
    return ans


def main():
    array = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6, 6, 7, 9, 10, 10, 10, 11, 11, 11]
    print(last(array, 4))
    print(first(array, 4))


if __name__ == "__main__":
    main()
