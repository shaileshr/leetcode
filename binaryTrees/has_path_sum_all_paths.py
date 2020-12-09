#Get all paths in a binary tree matching the sum

from binaryTrees.TreeNode import TreeNode
def get_all_paths(tree, remaining_sum):
    all_paths = []
    paths = []
    def get_all_paths_helper(tree, remaining_sum, paths):
        if not tree:
            return
        paths.append(tree.data)
        if not tree.left and not tree.right:
            if remaining_sum == tree.data:
                all_paths.append(list(paths))

        get_all_paths_helper(tree.left, remaining_sum- tree.data, paths)
        get_all_paths_helper(tree.right, remaining_sum- tree.data, paths)

        del paths[-1]
    get_all_paths_helper(tree, remaining_sum, paths)
    return all_paths

def main():
    tree1 = TreeNode(1, TreeNode(3), TreeNode(5))
    print(get_all_paths(tree1, 6))

    tree2 = TreeNode(1, TreeNode(3), TreeNode(5))
    print(get_all_paths(tree2, 4))

    tree3 = TreeNode(1, TreeNode(3), TreeNode(5))
    print(get_all_paths(tree3, 2))

    tree4 = TreeNode(1, TreeNode(3, TreeNode(6), None), TreeNode(5))
    print(get_all_paths(tree4, 10))

main()


