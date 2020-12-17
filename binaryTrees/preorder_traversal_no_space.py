from typing import List


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, result = None, []
    while tree:
        print(tree.data)
        if prev is tree.parent:
            result.append(tree.data)
            if tree.left:
                next = tree.left
            else:
                next = tree.right or tree.parent
        elif prev is tree.left:
            next = tree.right or tree.parent
        else:
            next = tree.parent

        prev, tree = tree, next
    return result

def main():
    t0 = BinaryTreeNode(1, None, None, None)
    t1 = BinaryTreeNode(3, None, None, t0)
    t0.left = t1
    t2 = BinaryTreeNode(5, None, None, t0)
    t0.right = t2
    #tree1 = BinaryTreeNode(1, BinaryTreeNode(3), BinaryTreeNode(5), None)
    print(preorder_traversal(t0))

    #tree2 = BinaryTreeNode(0, tree1, BinaryTreeNode(10), None)
    #print(preorder_traversal(tree2))

    #tree3 = BinaryTreeNode(20, tree1, tree2)
    #print(preorder_traversal(tree3))

    #tree4 = BinaryTreeNode(1, tree2, tree3)
    #print(preorder_traversal(tree4))

main()
