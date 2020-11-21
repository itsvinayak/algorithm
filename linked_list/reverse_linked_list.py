class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node,current.next = current.next,previous
            previous,current = current,next_node
        self.head = previous

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def main():
    ll = LinkedList()
    ll.push(2)
    ll.push(1)
    ll.push(3)
    ll.push(2)
    ll.reverse()
    ll.printLL()


if __name__ == "__main__":
    main()
