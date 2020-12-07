#EPI 9.1

#Check if tree is height balanced or not

from binaryTrees.TreeNode import TreeNode
from collections import namedtuple
def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def is_balanced_binary_tree(node):
        if not node:
            return BalancedStatusWithHeight(True, 0)

        left_tree_status = is_balanced_binary_tree(node.left)

        if not left_tree_status.balanced:
            return left_tree_status

        right_tree_status = is_balanced_binary_tree(node.right)
        if not right_tree_status.balanced:
            return right_tree_status

        is_balanced = abs(left_tree_status.height - right_tree_status.height) <= 1

        return BalancedStatusWithHeight(is_balanced, \
            max(left_tree_status.height, right_tree_status.height)+1)

    return is_balanced_binary_tree(tree)