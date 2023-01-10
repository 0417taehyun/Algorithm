# [ LeetCode ] 100. Same Tree

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


def solution(p: TreeNode | None, q: TreeNode | None) -> bool:
    def is_identical_same(
        p_node: TreeNode | None,
        q_node: TreeNode | None
    ) -> bool:
        if not p_node and not q_node:
            return True
        if (p_node and q_node) and (p_node.val == q_node.val):
            return True
        return False


    stack: list[list[TreeNode | None]] = [[p, q]]
    while stack:
        p_node, q_node = stack.pop()
        if not is_identical_same(p_node, q_node):
            return False
        
        if p_node and q_node:
            stack.append([p_node.right, q_node.right])
            stack.append([p_node.left, q_node.left])

    return True
