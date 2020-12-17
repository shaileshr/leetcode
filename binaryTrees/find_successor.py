from binaryTrees.TreeNode import TreeNode
from typing import Optional
# EPI
# leetcode: https://leetcode.com/problems/inorder-successor-in-bst-ii/
def find_successor(node: TreeNode) -> Optional[TreeNode]:
    # Case 1 Check left most node in  right subtree
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    # Case 2: Not right node, check parent iteratively. Stop when left subtree is exited
    while node.parent and node.parent.right is node:
        node = node.parent

    return node.parent