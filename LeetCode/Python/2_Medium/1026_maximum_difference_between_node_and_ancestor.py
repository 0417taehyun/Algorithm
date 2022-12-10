# [ LeetCode ] 1026. Maximum Difference Between Node and Ancestor

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
    def preorder_traverse(node: TreeNode, nodes: list[int]) -> None:
        nonlocal answer
        if node:
            nodes.append(node.val)
            if not node.left and not node.right:
                max_node: int = max(nodes)
                min_node: int = min(nodes)
                target: int = max_node - min_node
                if target > answer:
                    answer = target
            
            if node.left:
                preorder_traverse(node.left, nodes.copy())
            if node.right:
                preorder_traverse(node.right, nodes.copy())
    
    
    answer: int = 0
    nodes: list[int] = [root.val]
    preorder_traverse(root, nodes)
    return answer


def another_solution(root: TreeNode) -> int:
    def preorder_traverse(
        node: TreeNode, minimum_node: int, maximum_node: int
    ) -> None:
        nonlocal answer
        if node:
            if node.val > maximum_node:
                maximum_node = node.val
            elif node.val < minimum_node:
                minimum_node = node.val
            
            if not node.left and not node.right:
                target: int = maximum_node - minimum_node
                if target > answer:
                    answer = target
            if node.left:
                preorder_traverse(node.left, minimum_node, maximum_node)
            if node.right:
                preorder_traverse(node.right, minimum_node, maximum_node)
    
    
    answer: int = 0
    minimum_node: int = root.val
    maximum_node: int = root.val
    preorder_traverse(root, minimum_node, maximum_node)
    return answer
