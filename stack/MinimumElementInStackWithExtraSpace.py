class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def top(self):
        return self.stack[-1] if len(self.stack) != 0 else None

    def pop(self):
        return self.stack.pop()


class minimum_element_in_stack_with_extra_space:
    def __init__(self):
        self.s = Stack()
        self.ss = Stack()

    def push(self, element):
        self.s.push(element)
        if self.ss.top() is None or self.ss.top() >= element:
            self.ss.push(element)

    def pop(self):
        if self.s.top() is None:
            return -1
        ans = self.s.top()
        self.s.pop()
        if self.ss.top() == ans:
            self.ss.pop()
        return ans

    def get_min(self):
        if self.ss.top() is None:
            return -1
        return self.ss.pop()


def main():
    min_element = minimum_element_in_stack_with_extra_space()
    min_element.push(5)
    min_element.push(1)
    min_element.push(0)
    min_element.push(6)
    print(min_element.get_min())
    min_element.pop()
    min_element.pop()
    print(min_element.get_min())


if __name__ == "__main__":
    main()
