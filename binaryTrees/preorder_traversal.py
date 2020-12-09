from binaryTrees.TreeNode import TreeNode

def preorder_traversal(tree: TreeNode):
    # TODO - you fill in here.
    # stack = []
    # result = []
    # current = tree
    #
    # while current or stack:
    #     while current:
    #         result.append(current.data)
    #         if current.right:
    #             stack.append(current.right)
    #         current = current.left
    #     if stack:
    #         current = stack.pop()
    # return result

    result = []
    stack = [tree]

    while stack:
        current = stack.pop()
        if current:
            result.append(current.data)
            stack += [current.right, current.left]

    return result