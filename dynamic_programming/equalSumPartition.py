# same as is subset
def equalSumPartition(arr, n, k):
    if k == 0:
        return True
    elif n == 0 and k != 0:
        return False
    elif arr[n - 1] > k:
        return equalSumPartition(arr, n - 1, k)
    else:
        return equalSumPartition(arr, n - 1, k - arr[n - 1]) or equalSumPartition(
            arr, n - 1, k
        )


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        k = sum(arr)
        if k % 2 == 0:
            if equalSumPartition(arr, n, k / 2):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


if __name__ == "__main__":
    main()
