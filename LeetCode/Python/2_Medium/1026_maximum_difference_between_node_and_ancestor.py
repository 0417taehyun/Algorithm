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
