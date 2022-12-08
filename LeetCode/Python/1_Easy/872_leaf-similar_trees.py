# [ LeetCode ] 872. Leaf-Similar Trees

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


def is_leaf_node(node: TreeNode) -> bool:
    return not node.left and not node.right


def get_leaf_nodes(root: TreeNode) -> list[int]:
    nodes: list[int] = []
    stack: list[TreeNode] = [root]
    while stack:
        node: TreeNode = stack.pop()
        if is_leaf_node(node):
            nodes.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return nodes


def has_same_leaf_nodes(root1_leaf_nodes: list[int], root2_leaf_nodes: list[int]) -> bool:
    if len(root1_leaf_nodes) != len(root2_leaf_nodes):
        return False
    for root1_leaf_node, root2_leaf_node in zip(root1_leaf_nodes, root2_leaf_nodes):
        if root1_leaf_node != root2_leaf_node:
            return False
    return True


def solution(root1: TreeNode, root2: TreeNode) -> bool:
    root1_leaf_nodes: list[int] = get_leaf_nodes(root1)
    root2_leaf_nodes: list[int] = get_leaf_nodes(root2)

    return has_same_leaf_nodes(root1_leaf_nodes, root2_leaf_nodes)
