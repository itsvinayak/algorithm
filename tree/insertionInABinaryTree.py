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

    def insert(self, element):
        queue = []
        queue.append(self.root)

        while len(queue):
            temp = queue[0]
            queue.pop(0)

            if not temp.left:
                temp.left = Node(element)
                break
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = Node(element)
                break
            else:
                queue.append(temp.right)

    def __str__(self):
        return self.__printInorder(self.root)

    def __printInorder(self, node, traversal=""):
        """
        print tree in inorder
        """
        if node is not None:
            traversal = self.__printInorder(node.left, traversal)
            traversal += str(node.data) + " - "
            traversal = self.__printInorder(node.right, traversal)
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
    tree.insert(8)
    tree.insert(10)
    print(tree)


if __name__ == "__main__":
    main()
