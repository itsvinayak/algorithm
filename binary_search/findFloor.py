def floor(array, element):
    low = 0
    high = len(array) - 1

    while high >= low:
        mid = (low + high) // 2
        if element == array[mid]:
            return mid
        elif element < array[mid]:
            ans = low
            high = mid - 1
        else:
            low = mid + 1
    return ans


def main():
    array = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 18, 20]
    element = 5
    print(floor(array, element))


if __name__ == "__main__":
    main()
