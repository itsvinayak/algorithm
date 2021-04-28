def l_max(arr):
    ans = [None] * len(arr)
    ans[0] = arr[0]
    for i in range(1, len(arr)):
        ans[i] = max(ans[i - 1], arr[i])
    return ans


def r_max(arr):
    length = len(arr)
    ans = [None] * length
    ans[length - 1] = arr[length - 1]
    for i in range(length - 2, -1, -1):
        ans[i] = max(ans[i + 1], arr[i])
    return ans


def rain_water_tapping(arr):
    length = len(arr)
    ans = 0
    lmax = l_max(arr)
    rmax = r_max(arr)
    for i in range(length):
        temp = min(lmax[i], rmax[i]) - arr[i]
        ans += temp
    return ans


def main():
    arr = [3, 0, 0, 2, 0, 4]
    print(rain_water_tapping(arr))


if __name__ == "__main__":
    main()
