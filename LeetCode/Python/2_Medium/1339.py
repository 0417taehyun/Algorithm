# [ LeetCode ] 1339. Maximum Product of Splitted Binary Tree

class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" = None,
        right: "TreeNode" = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode) -> int:
    def get_total_nodes_sum(root: TreeNode) -> int:
        total: int = 0
        stack: list[TreeNode] = [root]
        while stack:
            node: TreeNode = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            total += node.val
        return total


    def postorder_traverse(
        node: TreeNode, total_nodes_sum: int
    ) -> int:
        if node:
            nonlocal answer
            left_subtree_nodes_sum: int = postorder_traverse(
                node.left, total_nodes_sum
            )
            left_target: int = left_subtree_nodes_sum * (
                total_nodes_sum - left_subtree_nodes_sum
            )
            right_subtree_nodes_sum: int = postorder_traverse(
                node.right, total_nodes_sum
            )
            right_target: int = right_subtree_nodes_sum * (
                total_nodes_sum - right_subtree_nodes_sum
            )
            if left_target > answer:
                answer = left_target
            if right_target > answer:
                answer = right_target
            return left_subtree_nodes_sum + right_subtree_nodes_sum + node.val

        return 0


    MOD: int = 10 ** 9 + 7
    answer: int = 0
    total_nodes_sum: int = get_total_nodes_sum(root)
    total_left_subtree_sum: int = postorder_traverse(
        root.left, total_nodes_sum
    )
    total_right_subtree_sum: int = postorder_traverse(
        root.right, total_nodes_sum
    )
    left_target: int = total_left_subtree_sum * (
        total_nodes_sum - total_left_subtree_sum
    )
    right_target: int = total_right_subtree_sum * (
        total_nodes_sum - total_right_subtree_sum
    )
    answer = max(left_target, right_target, answer)
    answer %= MOD
    return answer
    