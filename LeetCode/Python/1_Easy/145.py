# [ LeetCode ] 145. Binary Tree Postorder Traversal

def solution(root: "TreeNode") -> list[int]:
    def postorder_traverse(node: TreeNode) -> None:
        nonlocal answer            
        if node:
            if node.left:
                postorder_traverse(node=node.left)
                
            if node.right:
                postorder_traverse(node=node.right)
            
            answer.append(node.val)
            
            
    answer: list[int]  = []
    postorder_traverse(node=root)
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
    
    
    def create_binary_tree(index: int, items: list[int]) -> TreeNode:
        if items[index]:
            root: TreeNode = TreeNode(val=items[index])
            if (index*2+1) < len(items):
                root.left: TreeNode | None = create_binary_tree(
                    index=index*2+1, items=items
                )
            
            if (index*2+2) < len(items):
                root.right: TreeNode | None = create_binary_tree(
                    index=index*2+2, items=items
                )
            
            return root
            
        else:
            return None
    
        
    cases: list = [
        {
            "input": { "items": [1, None, 2, None, None, 3, None] },
            "output": [3, 2, 1]
        },
        {
            "input": { "items": [None] },
            "output": []
        },         
        {
            "input": { "items": [1] },
            "output": [1]
        }        
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["items"])
        )
        