# EPI

class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def lca_with_parent(node1, node2):
    def get_depth(node):
        depth = 0
        current = node
        while current:
            depth += 1
            current = current.parent

        return depth

    depth1, depth2 = get_depth(node1), get_depth(node2)
    if depth1 > depth2:
        node1, node2, depth1, depth2 = node2, node1, depth2, depth1

    depth_diff = depth2 - depth1

    for _ in depth_diff:
        node2 = node2.parent
        depth_diff -= 1

    while node1 is not node2:
        node1, node2 = node1.parent, node2.parent

    return node1