#  arr: [1 ,3 ,2 ,4]
#  ans: [-1 ,1 ,1 ,2]
#
#  arr: [4 ,5 ,2 ,10 ,8]
#  ans: [-1,4,-1,2,2]


# simple
def NSLSimple(arr):
    length = len(arr)
    for i in range(0, length):
        ans = -1
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                ans = arr[j]
                break
        print(arr[i], " - ", ans)


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack.pop()

    def top(self):
        return self.stack[-1]


def NSLStack(arr):
    length = len(arr)
    s = Stack()
    ans = []
    for i in range(0, length):
        if s.isEmpty():
            ans.append(-1)
        else:
            if s.top() < arr[i]:
                ans.append(s.top())
            else:
                while not s.isEmpty() and s.top() >= arr[i]:
                    s.pop()
                if s.isEmpty():
                    ans.append(-1)
                else:
                    ans.append(s.top())
        s.push(arr[i])
    return ans


def main():
    arr = [4, 5, 2, 10, 8]
    NSLSimple(arr)
    print(NSLStack(arr))


if __name__ == "__main__":
    main()
