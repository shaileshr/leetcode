# EPI
from binaryTrees.TreeNode import TreeNode

def sum_binary_path(tree):

    def sum_binary_path_helper(tree, sum_so_far):
        if not tree:
            return 0

        sum_so_far = 2 * sum_so_far + tree.data

        if not tree.left and not tree.right:
            return sum_so_far

        return sum_binary_path_helper(tree.left, sum_so_far) + \
               sum_binary_path_helper(tree.right, sum_so_far)

    return sum_binary_path_helper(tree, 0.0)
