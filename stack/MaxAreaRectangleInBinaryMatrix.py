class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, index, element):
        self.stack.append([index, element])

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def top(self):
        return self.stack[-1]


def NSL(arr):
    length = len(arr)
    s = Stack()
    pseudo = -1
    ans = []

    for i in range(length):
        if s.isEmpty():
            ans.append(pseudo)
        else:
            if s.top()[1] < arr[i]:
                ans.append(s.top()[0])
            else:
                while not s.isEmpty() and s.top()[1] >= arr[i]:
                    s.pop()
                if s.isEmpty():
                    ans.append(pseudo)
                else:
                    ans.append(s.top()[0])
        s.push(i, arr[i])
    return ans


def NSR(arr):
    length = len(arr)
    s = Stack()
    pseudo = length
    ans = []

    for i in range(length - 1, -1, -1):
        if s.isEmpty():
            ans.append(pseudo)
        else:
            if s.top()[1] < arr[i]:
                ans.append(s.top()[0])
            else:
                while not s.isEmpty() and s.top()[1] >= arr[i]:
                    s.pop()
                if s.isEmpty():
                    ans.append(pseudo)
                else:
                    ans.append(s.top()[0])
        s.push(i, arr[i])
    return ans[::-1]


def LargestAreaHistogram(arr):
    leftArr = NSL(arr)
    rightArr = NSR(arr)
    length = len(arr)
    width = []
    ans = -1

    for i in range(length):
        width.append((rightArr[i] - leftArr[i]) - 1)
    for i in range(length):
        temp = width[i] * arr[i]
        ans = max(ans, temp)

    return ans


def MaxAreaRectangleInBinaryMatrix(arr2d):
    temp = arr2d[0]
    ans = -1
    for j in range(1, len(arr2d)):
        arr1d = arr2d[j]
        for i in range(len(arr1d)):
            temp[i] = (temp[i] + arr1d[i]) * arr1d[i]
        ans = max(ans, LargestAreaHistogram(temp))
    return ans


def main():
    arr2d = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
    print(MaxAreaRectangleInBinaryMatrix(arr2d))


if __name__ == "__main__":
    main()
