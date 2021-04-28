# 50 ->  20 -> 15 -> 4 -> 10
#              |           |
#              -------------
#
# D = 50 -> 20
# k = extra loop node
# c = loop
# 2sp = fp
# sp = D+K+c(i)
# fp = 2D+2K+c(2j)
# fp - sp
# D = c(i-2j) - k ## now think


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def findStatingOfLoop(self):

        fast = self.head
        slow = self.head

        slow = slow.next
        fast = fast.next.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        if fast != slow:
            return None

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data


def main():
    ll = LinkedList()
    ll.head = Node(50)
    ll.head.next = Node(20)
    ll.head.next.next = Node(15)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(10)

    ll.head.next.next.next.next.next = ll.head.next.next

    print(ll.findStatingOfLoop())


if __name__ == "__main__":
    main()
