class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = {}

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def count_occurrence(self):
        temp = self.head
        while temp:
            if temp.data in self.count:
                self.count[temp.data] += 1
            else:
                self.count[temp.data] = 1
            temp = temp.next
        return self.count

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
    print(ll.count_occurrence())
    ll.printLL()


if __name__ == "__main__":
    main()
