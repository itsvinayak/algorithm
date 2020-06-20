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
        else:
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
    print(leftArr)
    print(rightArr)
    length = len(arr)
    width = []
    ans = -1

    for i in range(length):
        width.append((rightArr[i] - leftArr[i]) - 1)
    print(width)
    for i in range(length):
        temp = width[i] * arr[i]
        ans = max(ans, temp)

    return ans


def main():
    arr = [6, 2, 5, 4, 5, 1, 6]
    print(LargestAreaHistogram(arr))


if __name__ == "__main__":
    main()
