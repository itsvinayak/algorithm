class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def detectLoop(self):
        fast = self.head
        slow = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return 1
        return 0


def main():
    ll = LinkedList()
    ll.push(2)
    ll.push(3)
    ll.push(9)
    ll.push(3)
    ll.head.next.next.next.next = ll.head
    print(ll.detectLoop())


if __name__ == "__main__":
    main()
