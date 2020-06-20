class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def top(self):
        return self.stack[:-1] if len(self.stack) != 0 else None

    def pop(self):
        return self.stack.pop()


class minimum_element_in_stack_with_extra_space:
    def __init__(self):
        self.s = Stack()
        self.ss = Stack()

    def push(self, element):
        self.s.push(element)
        if self.ss.top is not None or self.ss.top() >= element:
            self.ss.push(element)

    def pop(self):
        pass

    def get_min(self):
        if self.ss.top() is None:
            return -1
        return self.ss.pop()


def main():
    arr = [1, 2, 0, 1, 4, 8]
    print(minimum_element_in_stack_with_extra_space(arr))
    arr = [1, 2, 3, 2, 1]
    print(minimum_element_in_stack_with_extra_space(arr))


if __name__ == "__main__":
    main()
