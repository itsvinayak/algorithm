def MagicIndex(array, index):
    if array[index] == index + 1:
        return True
    elif index == len(array) - 1:
        return False
    else:
        return MagicIndex(array, index + 1)


def main():
    array = [1, 2, 3, 4, 6, 7, 8, 2, 5, 0, 1]
    print(MagicIndex(array, 0))


if __name__ == "__main__":
    main()
