def sort(array):
    if len(array) == 1:
        return

    temp = array.pop()
    sort(array)
    insert(array, temp)


def insert(array, n):
    if len(array) == 0 or array[len(array) - 1] <= n:
        array.append(n)
        return
    temp = array.pop()
    insert(array, n)
    array.append(temp)


def main():
    array = [1, 3, 2, 4, 5, 6, 7, 9]
    print(*array)
    sort(array)
    print(*array)


if __name__ == "__main__":
    main()
