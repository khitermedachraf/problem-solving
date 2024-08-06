class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def getHeight(root):
    if root is None:
        return -1
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    return 1 + max(left_height, right_height)

