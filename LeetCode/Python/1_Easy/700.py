# [ LeetCode ] 700. Search in a Binary Search Tree

class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None
    ):
        self.val = val
        self.left = left
        self.right = right
        
        
def solution(root: TreeNode, val: int) -> TreeNode | None:
    stack: list[TreeNode] = [root]
    while stack:
        node: TreeNode = stack.pop()
        if node.val == val:
            return node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return None


def another_solution(root: TreeNode, val: int) -> TreeNode | None:
    while root:
        if root.val > val:
            root = root.left
        elif root.val < val:
            root = root.right
        else:
            return root
    return None
