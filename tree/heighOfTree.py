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

    def __maxDepthUtil(self, node):
        if node is None:
            return 0
        else:
            lDepth = self.__maxDepthUtil(node.left)
            rDepth = self.__maxDepthUtil(node.right)

            return lDepth + 1 if lDepth > rDepth else rDepth + 1

    def maxDepth(self):
        node = self.root
        print(self.__maxDepthUtil(node))

    def __str__(self):
        return self.printInorder(self.root)

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
    tree.maxDepth()


if __name__ == "__main__":
    main()
