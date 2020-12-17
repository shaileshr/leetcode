from typing import List

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    # TODO - you fill in here.
    def is_leaf(node):
        if not node.left and not node.right:
            return True
        return False

    def left_exterior(subtree, is_boundary):
        if not subtree:
            return []

        return ([subtree] if is_boundary or is_leaf(subtree) else []) + \
            (left_exterior(subtree.left, is_boundary)) + \
            (left_exterior(subtree.right, is_boundary and not subtree.left))

    def right_exterior(subtree, is_boundary):
        if not subtree:
            return []

        return (right_exterior(subtree.left, is_boundary and not subtree.right)) + \
            (right_exterior(subtree.right, is_boundary)) + \
            ([subtree] if is_leaf(subtree) or is_boundary else [])

    return ([tree] + left_exterior(tree.left, True) + right_exterior(tree.right, True) if tree else [])
