# [ LeetCode ] 938. Range Sum of BST

class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" = None,
        right: "TreeNode" = None
    ):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode, low: int, high: int) -> int:
    answer: int = 0
    stack: list[TreeNode] = [root]
    while stack:
        node: TreeNode = stack.pop()
        if node.val > high and node.left:
            stack.append(node.left)
        elif node.val < low and node.right:
            stack.append(node.right)
        elif node.val >= low and node.val <= high:
            answer += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return answer
