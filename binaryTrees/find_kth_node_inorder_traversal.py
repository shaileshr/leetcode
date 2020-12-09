
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int):
    # TODO - you fill in here.
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size+1<k:
            k -= left_size +1
            tree = tree.right
        elif left_size == k-1:
            return tree
        else:
            tree = tree.left
    return None