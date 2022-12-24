# [ LeetCode ] 298. Binary Tree Longest Consecutive Sequence

def solution(root: "TreeNode") -> int:
    def preorder_traverse(depth: int, node: TreeNode) -> int:
        if node:
            from_left_depth, from_right_depth = depth, depth
            if node.left:
                if node.left.val == node.val + 1:
                    from_left_depth = preorder_traverse(depth=depth+1, node=node.left)
                else:
                    from_left_depth = max(
                        from_left_depth, preorder_traverse(depth=1, node=node.left)
                    )
            if node.right:
                if node.right.val == node.val + 1:
                    from_right_depth = preorder_traverse(depth=depth+1, node=node.right)
                else:
                    from_right_depth = max(
                        from_right_depth, preorder_traverse(depth=1, node=node.right)
                    )
            
            return max(from_left_depth, from_right_depth)
        
        else:
            return depth
    
    
    answer = preorder_traverse(depth=1, node=root)
    return answer


if __name__ == "__main__":
    class TreeNode:
        def __init__(
            self,
            val: int,
            left: "TreeNode" = None,
            right: "TreeNode" = None
        ) -> None:   
            self.val = val
            self.left = left
            self.right = right

            
    cases: list[dict[str, dict[str, list[int | None]] | list[int | None]]] = [
        {
            "input": { "items": [[1, None, 3, 2, 4, None, None, None, 5]] },
            "output": 3
        },
        {
            "input": { "items": [2, None, 3, 2, None, 1] },
            "output": 2
        },              
    ]