# [ LeetCode ] 404. Sum of Left Leaves

def solution(root: "TreeNode") -> int:
    def postorder_traverse(node: "TreeNode", is_left: bool) -> None:
        nonlocal answer
        if node:
            if node.left or node.right:
                if node.left:
                    postorder_traverse(node=node.left, is_left=True)
                if node.right:
                    postorder_traverse(node=node.right, is_left=False)
            
            elif is_left:
                answer += node.val
            
            
    answer: int = 0
    postorder_traverse(node=root, is_left=False)
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
            root : TreeNode = TreeNode(val=items[index])
            if (index*2+1) < len(items):
                root.left: TreeNode = create_binary_tree(
                    index=index*2+1, items=items
                )
            
            if (index*2+2) < len(items):
                root.right: TreeNode = create_binary_tree(
                    index=index*2+2, items=items
                )
            
            return root
            
        else:
            return None
    
    
    cases: list[dict[str, dict[str, list[int | None]] | int]] = [
        {
            "input": { "items": [3, 9, 20, None, None, 15, 7] },
            "output": 24
        },
        {
            "input": { "items": [1] },
            "output": 0
        }        
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["items"])
        )
        