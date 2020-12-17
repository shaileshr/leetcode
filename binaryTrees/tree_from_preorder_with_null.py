from typing import List

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    def reconstruct_preorder_helper(preorer_iter):
        root = next(preorer_iter)
        if not root:
            return None

        left_tree = reconstruct_preorder_helper(preorer_iter)
        right_tree = reconstruct_preorder_helper(preorer_iter)

        return BinaryTreeNode(root, left_tree, right_tree)
    return reconstruct_preorder_helper(iter(preorder))
