# Implement an algorithm to find if the linked list is palindrome 


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

    def isPalindrome(self):
      # 1 2 3 2 1
      return self._isPalindromeUtil(self.head, False)

    def _isPalindromeUtil(self,node = None,boolVal = False):
      temp = node.data
      if node.next is None:
        if temp == node.data:
          return True
        else:
          return False
      else:
        self._isPalindromeUtil(node.next)



if __name__ == "__main__":
    ll = LinkedList()
    ll.makeNode(1)
    ll.makeNode(2)
    ll.makeNode(1)
    ll.makeNode(4)
    ll.printLinkedList()
