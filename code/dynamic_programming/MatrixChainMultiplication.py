import sys


def MatrixChainMultiplicationRec(array, i, j):
    if i == j:
        return 0
    minn = sys.maxsize

    for k in range(i, j):
        count = (
            MatrixChainMultiplicationRec(array, i, k)
            + MatrixChainMultiplicationRec(array, k + 1, j)
            + (array[i - 1] * array[k] * array[j])
        )
        minn = min(minn, count)

    return minn


def main():
    array = [1, 2, 3, 4, 3]
    print(MatrixChainMultiplicationRec(array, 1, len(array)-1))


if __name__ == "__main__":
    main()
