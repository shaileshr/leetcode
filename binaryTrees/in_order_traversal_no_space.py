from typing import List


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    prev, result = None, []
    while tree:
        if tree.parent is prev:
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
        elif tree.left is prev:
            result.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent

        prev, tree = tree, next

    return result