# Find the largest Complete Subtree in a given Binary Tree
# Last Updated: 19-02-2020
# Given a Binary Tree, the task is to find the size of largest Complete sub-tree in the given Binary Tree.
# Complete Binary Tree – A Binary tree is Complete Binary Tree if all levels are completely filled except possibly the
# last level and the last level has all keys as left as possible.
#
# Note: All Perfect Binary Trees are Complete Binary tree but reverse in NOT true. If a tree is not complete then it is
# also not Perfect Binary Tree.
#
# Examples:
#
# Input:
#               1
#            /     \
#           2        3
#         /   \     /  \
#        4      5   6   7
#      /  \    /
#     8   9   10
# Output:
# Size : 10
# Inorder Traversal : 8 4 9 2 10 5 1 6 3 7
# The given tree a complete binary tree.
#
# Input:
#          50
#       /      \
#    30         60
#   /   \      /    \
#  5    20   45      70
#           /
#          10
# Output:
# Size : 4
# Inorder Traversal : 10 45 60 70

from collections import namedtuple
from binaryTrees.TreeNode import TreeNode
def largest_complete_tree(tree):
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height', 'size'))
    max_size = [float('-inf')]

    def largest_complete_tree_helper(node):
        if not node:
            return BalancedStatusWithHeight(True, 0, 0)

        left_tree_status = largest_complete_tree_helper(node.left)

        if not left_tree_status.balanced:
            return left_tree_status

        right_tree_status = largest_complete_tree_helper(node.right)
        if not right_tree_status.balanced:
            return right_tree_status

        is_balanced = abs(left_tree_status.height - right_tree_status.height) <= 1
        size = left_tree_status.size + right_tree_status.size + 1
        height = max(left_tree_status.height, right_tree_status.height)+1

        if is_balanced:
            max_size[0] = max(max_size[0], size)
        else:
            size = 0

        return BalancedStatusWithHeight(is_balanced, \
            height, size)


    largest_complete_tree_helper(tree)
    print(max_size[0])
    return max_size[0]

def main():
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))
    print(largest_complete_tree(tree))

    tree2 = TreeNode(50, TreeNode(30, TreeNode(5), TreeNode(20)), TreeNode(60, TreeNode(45, TreeNode(10), None), TreeNode(70)))
    print(largest_complete_tree(tree2))

main()