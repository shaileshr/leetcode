# EPI
from binaryTrees.TreeNode import TreeNode

def is_symmetric(tree):

    def is_symmetric_helper(node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False

        return node1.val == node2.val and \
               is_symmetric_helper(node1.left, node2.right) and \
               is_symmetric_helper(node1.right, node2.left)

    return not tree or is_symmetric_helper(tree.left, tree.right)
