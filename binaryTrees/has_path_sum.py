from binaryTrees.TreeNode import TreeNode
def has_path_sum(tree: TreeNode, remaining_weight: int) -> bool:
    # TODO - you fill in here.
    def has_path_sum_helper(tree, remaining_weight):
        if not tree:
            return False

        sum = remaining_weight - tree.data

        if not tree.left and not tree.right:
            return sum == 0

        return has_path_sum_helper(tree.left, sum) or has_path_sum_helper(tree.right, sum)

    return has_path_sum_helper(tree, remaining_weight)
