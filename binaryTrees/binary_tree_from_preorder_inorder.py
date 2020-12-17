from typing import List

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    node_idx = {node : index for index, node in enumerate(inorder)}
    def binary_tree_from_preorder_inorder_helper(pre_order_start, pre_order_end, inorder_start, inorder_end):

        if pre_order_start >= pre_order_end:
            return None

        root = preorder[pre_order_start]
        root_idx = node_idx[root]
        left_tree_size = root_idx-inorder_start

        return BinaryTreeNode(root, \
            binary_tree_from_preorder_inorder_helper(pre_order_start+1, pre_order_start+left_tree_size+1, inorder_start, root_idx), \
            binary_tree_from_preorder_inorder_helper(pre_order_start+left_tree_size+1, pre_order_end, root_idx+1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))
