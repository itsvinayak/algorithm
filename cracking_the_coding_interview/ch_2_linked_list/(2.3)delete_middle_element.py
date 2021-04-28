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

    # Deletes middle node
    def deleteMiddleElement(self):
        # Base cases
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
            return None
        # Initialize slow and fast pointers to reach
        fast = self.head
        slow = self.head
        # Find the middle and previous of middle.
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # skiping middle element
        prev.next = slow.next


# Drier program to test above function
if __name__ == "__main__":
    ll = LinkedList()
    head = ll.makeNode(1)
    ll.makeNode(2)
    ll.makeNode(3)
    ll.makeNode(4)
    ll.makeNode(5)
    print("Gven Linked List ")
    ll.printLinkedList(head)
    ll.deleteMiddleElement()
    print("Linked List after deletion of middle")
    ll.printLinkedList(head)

# by vinayak
