# EPI
from binaryTrees.TreeNode import TreeNode
from collections import namedtuple


def lca(tree, node0, node1):
    Status = namedtuple('Status', ('num_nodes', 'ancestor'))

    def lca_helper(tree, node0, node1):

        if not tree:
            return Status(0, None)

        # Both nodes in left tree
        left_tree_status = lca_helper(tree.left, node0, node1)

        if left_tree_status.num_nodes == 2:
            return left_tree_status

        # Both trees in right node
        right_tree_status = lca_helper(tree.right, node0, node1)

        if right_tree_status.num_nodes == 2:
            return right_tree_status

        num_nodes = left_tree_status.num_nodes + right_tree_status.num_nodes + \
                    (node0, node1).count(tree)
        return Status(num_nodes, tree if num_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor
