class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def makeNode(self, val):
        if self.head is None:
            self.head = Node(val)
            return self.head
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

    def printLinkedList(self, node):
        if node is not None:
            print(node.val)
            ll.printLinkedList(node.next)

    def deleteMiddleElement(self):
        slow = self.head
        fast = self.head.next

        while fast.next.next:
            slow = slow.next

        print(fast.val)


if __name__ == "__main__":
    ll = LinkedList()
    head = ll.makeNode(1)
    ll.makeNode(2)
    ll.makeNode(1)
    ll.makeNode(4)
    ll.printLinkedList(head)
    ll.deleteMiddleElement()
    ll.printLinkedList(head)
