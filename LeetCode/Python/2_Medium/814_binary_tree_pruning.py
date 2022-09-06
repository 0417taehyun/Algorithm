# [ LeetCode ] 814. Binary Tree Pruning

def solution(root: "TreeNode") -> "TreeNode":
    def preorder_traverse(node: TreeNode) -> None | bool:
        if node:
            if not preorder_traverse(node=node.left):
                node.left = None
            if not preorder_traverse(node=node.right):
                node.right = None
            
            return node.val or node.left or node.right
    
    return root if preorder_traverse(node=root) else None


def another_solution(root: "TreeNode") -> "TreeNode":
    if not root:
        return None
    else:
        if not another_solution(root=root.left):
            root.left = None
        if not another_solution(root=root.right):
            root.right = None
        
        if not root.val or not root.left or not root.right:
            return None
        
        else:
            return root


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
            "input": {
                "items": [1, None, 0, None, None, 0, 1]
            },
            "output": [1, None, 0, None, 1]
        },
        {
            "input": {
                "items": [1, 0, 1, 0, 0, 0, 1]
            },
            "output": [1, None, 1, None, 1]
        },
        {
            "input": {
                "items": [
                    1, 1, 0, 1, 1, 0, 1, 0, None,
                    None, None, None, None, None, None
                ]
            },
            "output": [1, 1, 0, 1, 1, None, 1]
        },
               {
            "input": { "items": [0] },
            "output": []
        }                 
    ]
    