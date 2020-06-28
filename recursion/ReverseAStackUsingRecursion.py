class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def insertElementEnd(self, element):
        if self.isEmpty():
            self.push(element)
        else:
            temp = self.pop()
            self.insertElementEnd(element)
            self.push(temp)

    def reverse(self):
        if not self.isEmpty():
            temp = self.pop()
            self.reverse()
            self.insertElementEnd(temp)

    def printStack(self):
        print(self.stack)


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.printStack()
    s.reverse()
    s.printStack()


if __name__ == "__main__":
    main()
