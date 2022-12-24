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
        
        if not root.val and not root.left and not root.right:
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
    
    
    def convert_binary_tree_to_list(node: TreeNode):
        global nodes
        if node:
            nodes.append(node.val)
            if node.left or node.right:
                if node.left:
                    convert_binary_tree_to_list(node.left)
                else:
                    nodes.append(None)
                    
                if node.right:
                    convert_binary_tree_to_list(node.right)
                else:
                    nodes.append(None)
                

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
            "input": { "items": [0] },
            "output": []
        }                 
    ]
    for case in cases:
        nodes: list[int | None] = []
        convert_binary_tree_to_list(
            node=solution(
                root=create_binary_tree(index=0, items=case["input"]["items"])
            )
        )
        assert case["output"] == nodes
        
        nodes: list[int | None] = []
        convert_binary_tree_to_list(
            node=another_solution(
                root=create_binary_tree(index=0, items=case["input"]["items"])
            )
        )
        assert case["output"] == nodes
        