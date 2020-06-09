# Implement an algorithm to find the kth to last element of a singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def makeNode(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.makeNode(1)
    ll.makeNode(2)
    ll.makeNode(1)
    ll.makeNode(4)
    ll.printLinkedList()
