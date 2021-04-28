class Node:
    """
    single Node for tree
    """

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class binaryTree:
    """
    binary tree implementation
    """

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

    def __str__(self):
        return self.printInorder(self.root)

    def printPreorder(self, node, traversal=""):
        pass

    def printPostorder(self, node, traversal=""):
        pass

    def printLevelOrder(self, node):
        pass

    def printInorder(self, node, traversal=""):
        """
        print tree in inorder
        """
        if node is not None:
            traversal = self.printInorder(node.left, traversal)
            traversal += str(node.data) + " - "
            traversal = self.printInorder(node.right, traversal)
        return traversal


def main():
    """
    Main code and logic comes here
    """
    tree = binaryTree()
    tree.push(5)
    tree.push(3)
    tree.push(1)
    tree.push(3)
    tree.push(0)
    tree.push(2)
    tree.push(9)
    print(tree)


if __name__ == "__main__":
    main()
