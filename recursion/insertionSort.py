def insertionSort(array, length=None):
    if length is None:
        length = len(array)

    if length <= 1:
        return

    insertionSort(array, length - 1)

    key = array[length - 1]
    j = length - 2

    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key


def main():
    array = [1, 4, 2, 5, 2, 3, 5, 0, 9, 8]
    insertionSort(array)
    print(*array)


if __name__ == "__main__":
    main()
