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

    def printLinkedList(self, node):
        if node is not None:
            print(node.val)
            ll.printLinkedList(node.next)
