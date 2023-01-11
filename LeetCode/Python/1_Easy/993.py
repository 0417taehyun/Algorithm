# [ LeetCode ] 993. Cousins in Binary Tree

class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode | None, x: int, y: int) -> bool:
    def traverse(node: TreeNode | None, depth: int) -> None:
        nonlocal x_depth, y_depth, x_parent, y_parent
        if node:
            depth += 1
            if node.left:
                if node.left.val == x:
                    x_depth = depth
                    x_parent = node.val
                if node.left.val == y:
                    y_depth = depth
                    y_parent = node.val
                traverse(node=node.left, depth=depth)
            if node.right:
                if node.right.val == x:
                    x_depth = depth
                    x_parent = node.val
                if node.right.val == y:
                    y_depth = depth
                    y_parent = node.val
                traverse(node=node.right, depth=depth)


    x_depth, y_depth = 0, 0
    x_parent, y_parent = 0, 0
    traverse(node=root, depth=0)
    return x_depth == y_depth and x_parent != y_parent
