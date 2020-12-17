from typing import List

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    # TODO - you fill in here.
    #result = []
    #def create_list_of_leaves_helper(node):
    #     if not node:
    #         return
    #
    #     if not node.left and not node.right:
    #         result.append(node)
    #
    #     if node.left:
    #         create_list_of_leaves_helper(node.left)
    #     if node.right:
    #         create_list_of_leaves_helper(node.right)
    #
    # create_list_of_leaves_helper(tree)
    # return result

    if not tree:
        return []
    elif not tree.left and not tree.right:
        return [tree]
    else:
        return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)
