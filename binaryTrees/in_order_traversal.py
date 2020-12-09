from binaryTrees.TreeNode import TreeNode
def inorder_traversal(tree: TreeNode):
    stack = []
    result = []
    current = tree

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right

    return result
