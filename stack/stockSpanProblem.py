# simple


def stockSpanProblem(arr):
    length = len(arr)
    ans = [None] * length
    ans[0] = 1
    for i in range(1, length):
        ans[i] = 1

        j = i - 1
        while j >= 0 and arr[i] >= arr[j]:
            ans[i] += 1
            j -= 1

    print(ans)


class Stack:
    """
    class for creating stack DS
    function it have :
        push -> push value to stack
        pop -> return a value out of stack
        isEmpty -> return true if stack is empty
        top -> return value from stack without removing it
    """

    def __init__(self):
        self.stack = []

    def push(self, index, element):
        self.stack.append([index, element])

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def pop(self):
        return -1 if self.isEmpty() else self.stack.pop()

    def top(self):
        return self.stack[-1] if not self.isEmpty() else -1


def stockSpanProblemStack(arr):
    length = len(arr)
    s = Stack()

    ans = []

    for i in range(0, length):
        if s.isEmpty():
            ans.append(-1)
        else:
            if s.top()[1] > arr[i]:
                ans.append(s.top()[0])
            else:
                while not s.isEmpty() and s.top()[1] <= arr[i]:
                    s.pop()
                if s.isEmpty():
                    ans.append(-1)
                else:
                    ans.append(s.top()[0])
        s.push(i, arr[i])

    for i in range(length):
        ans[i] = i - ans[i]

    return ans


def main():
    arr = [10, 4, 5, 90, 120, 80]
    stockSpanProblem(arr)
    print(stockSpanProblemStack(arr))


if __name__ == "__main__":
    main()
