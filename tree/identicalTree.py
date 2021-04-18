class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self):
        self.root = None

    def _pushUtil(self, node, element):
        if element < node.data:
            if node.left is None:
                node.left = Node(element)
            else:
                self._pushUtil(node.left, element)
        else:
            if node.right is None:
                node.right = Node(element)
            else:
                self._pushUtil(node.right, element)

    def push(self, element):
        if self.root is None:
            self.root = Node(element)
        else:
            self._pushUtil(self.root, element)

    def printTree(self):
        self._printUtil(self.root)

    def _printUtil(self, node):
        if node is not None:
            self._printUtil(node.left)
            print(node.data, end=" - ")
            self._printUtil(node.right)


def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if (
        root1.data == root2.data
        and isIdentical(root1.left, root2.left)
        and isIdentical(root1.right, root2.right)
    ):
        return True
    else:
        return False


def main():
    bt1 = binaryTree()
    bt2 = binaryTree()
    bt1.push(1)
    bt1.push(2)
    bt1.push(3)
    bt1.push(4)
    bt2.push(1)
    bt2.push(2)
    bt2.push(3)
    bt2.push(4)
    bt1.printTree()
    print("\n")
    bt2.printTree()
    print(isIdentical(bt1.root, bt2.root))


if __name__ == "__main__":
    main()
