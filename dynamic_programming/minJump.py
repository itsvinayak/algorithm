def minJumpRec(arr, startIndex, endIndex):

    if startIndex == endIndex:
        return 0
    elif arr[startIndex] == 0:
        return -1
    else:
        minJump = 9999999999999
        for i in range(startIndex + 1, endIndex + 1):
            if i < startIndex + arr[startIndex] + 1:
                minJump = 1 + min(minJump, minJumpRec(arr, i, endIndex))
        return minJump


def minJumpDp(arr, n):
    jumps = [0 for i in range(n)]

    for i in range(1, n):
        jumps[i] = 9999999999999
        for j in range(i):
            if i <= j + arr[j]:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[n - 1]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(minJumpDp(arr, n))
