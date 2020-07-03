class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1]

    def __str__(self):
        return f" stack is {self.stack}"

    def insert(self, element):
        if self.isEmpty or self.top() <= element:
            self.push(element)
            return

        temp = self.pop()
        print(temp, " ", element)
        self.insert(element)
        self.push(temp)

    def sort(self):
        if len(self.stack) == 1:
            return

        temp = self.pop()
        self.sort()
        self.insert(temp)


def main():
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(0)
    s.push(2)
    s.push(8)
    s.push(2)
    print(s)
    s.sort()
    print(s)


if __name__ == "__main__":
    main()
