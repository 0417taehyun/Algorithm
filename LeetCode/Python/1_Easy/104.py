# [ LeetCode ] 104. Maximum Depth of Binary Tree

def solution(root: "TreeNode") -> int:
    def postorder_traverse(depth: int, node: TreeNode) -> int:
        if node:
            from_left_depth, from_right_depth = depth, depth
            if node.left:
                from_left_depth = postorder_traverse(
                    depth=depth+1, node=node.left
                )
            if node.right:
                from_right_depth = postorder_traverse(
                    depth=depth+1, node=node.right
                )
            
            return max(from_left_depth, from_right_depth)
            
        else:
            return depth
    
    
    answer: int = 0
    answer += postorder_traverse(depth=1, node=root)
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
        
    
    def create_binary_tree(index: int, items: list[int | None]) -> TreeNode:
        if items[index] != None:
            root: TreeNode = TreeNode(val=items[index])
            if (index * 2 + 1) < len(items):
                root.left = create_binary_tree(index=index*2+1, items=items)
            if (index * 2 + 2) < len(items):
                root.right = create_binary_tree(index=index*2+2, items=items)              
            
            return root
        
        else:
            return None
    
            
    cases: list[dict[str, dict[str, list[int | None]] | list[int | None]]] = [
        {
            "input": { "items": [3, 9, 20, None, None, 15, 7] },
            "output": 3
        },
        {
            "input": { "items": [1, None, 2] },
            "output": 2
        },              
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["items"])
        )
        