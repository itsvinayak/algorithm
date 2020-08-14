def insertionSort(array):
    length = len(array)

    for i in range(1, length):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            print(f"--> {array}")
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def main():
    array = [2, 1, 3, 4, 5, 7, 6, 9, 8]
    insertionSort(array)

    print(array)


if __name__ == "__main__":
    main()
