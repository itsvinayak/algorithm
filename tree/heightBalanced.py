class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class binaryTree:
    def __init__(self):
        self.root = None

    def push(self, element, node=None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(element)

        else:
            if element < node.data:
                if node.left is not None:
                    self.push(element, node.left)
                else:
                    node.left = Node(element)
            else:
                if node.right is not None:
                    self.push(element, node.right)
                else:
                    node.right = Node(element)

    def printInorder(self):
        print(self._printInorderUtil(self.root, ""))

    def _printInorderUtil(self, node, traversal):
        """
        print tree in inorder
        """
        if node is not None:
            traversal = self._printInorderUtil(node.left, traversal)
            traversal += str(node.data) + " - "
            traversal = self._printInorderUtil(node.right, traversal)
        return traversal

    def height(self):
        return self._heightUtil(self.root)

    def _heightUtil(self, node):
        if node is None:
            return 0

        return 1 + max(self._heightUtil(node.left), self._heightUtil(node.right))

    def heightBalanced(self):
        return self._heightBalancedUtil(self.root)

    def _heightBalancedUtil(self, node):
        if node is None:
            return True

        lh = self._heightUtil(node.left)
        lr = self._heightUtil(node.right)

        if (
            abs(lh - lr) <= 1
            and self._heightBalancedUtil(node.left)
            and self._heightBalancedUtil(node.right)
        ):
            return True
        else:
            return False


def main():
    t = binaryTree()
    t.push(1)
    t.push(2)
    t.push(3)
    t.push(0)
    t.push(7)
    t.push(8)
    t.push(6)
    t.push(6)
    t.push(6)
    t.printInorder()
    print(t.heightBalanced())


if __name__ == "__main__":
    main()
