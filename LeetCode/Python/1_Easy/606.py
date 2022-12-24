# [ LeetCode ] 606. Construct String from Binary Tree

def solution(root: "TreeNode") -> str:
    def preorder_traverse(node: TreeNode) -> None:
        nonlocal answer
        if node:
            answer += str(node.val)
            if node.left:
                answer += str("(")
                preorder_traverse(node=node.left)
                answer += str(")")
            
            if node.right:
                answer += str("(")
                if not node.left:
                    answer += str(")(")
                
                preorder_traverse(node=node.right)
                answer += str(")")
        

    answer: str = ""
    preorder_traverse(node=root)
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
    
    
    cases: list[dict[str, dict[str, list[int | None]] | str]] = [
        {
            "input": { "items": [1, 2, 3, 4] },
            "output": "1(2(4))(3)"
        },
        {
            "input": { "items": [1, 2, 3, None, 4] },
            "output": "1(2()(4))(3)"
        }        
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["items"])
        )