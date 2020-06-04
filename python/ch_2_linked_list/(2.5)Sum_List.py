class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def makeNode(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        return self.head

    def printLinkedList(self, node):
        if node is not None:
            print(node.data, end="--> ")
            self.printLinkedList(node.next)

    def SumList(l1, l2, carry):
        pass


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()

    head1 = l1.makeNode(7)
    head2 = l2.makeNode(5)

    l1.makeNode(1)
    l1.makeNode(6)

    l2.makeNode(9)
    l2.makeNode(2)

    print("Gven Linked List ")
    l1.printLinkedList(head1)
    print("null")
    l2.printLinkedList(head2)
    print("null")
