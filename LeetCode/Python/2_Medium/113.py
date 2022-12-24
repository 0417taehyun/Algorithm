# [ LeetCode ] 113. Path Sum II

def solution(root: "TreeNode", targetSum: int) -> bool:
    def inorder_traverse(values: list[int], node: TreeNode) -> None:
        nonlocal answer
        if node:
            values.append(node.val)
            if node.left or node.right:
                if node.left:
                    inorder_traverse(values=values.copy(), node=node.left)
                if node.right:
                    inorder_traverse(values=values.copy(), node=node.right) 
            
            elif sum(values) == targetSum:
                answer.append(values)

    
    answer: list[list[int]] = []
    inorder_traverse(values=[], node=root)
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
        if items[index]:
            root: TreeNode = TreeNode(val=items[index])

            if index * 2 + 1 < len(items):
                root.left = create_binary_tree(index=index*2+1, items=items)
            if index * 2 + 2 < len(items):
                root.right = create_binary_tree(index=index*2+2, items=items)
        
            return root

    
    
    cases: list[dict[str, dict[str, list[int | None] | int]  | bool]] = [
        {
            "input": {
                "items": [
                    5, 4, 8, 11, -2, 13, 4, 7, 2, -3, -4, None, None, 5, 1
                ],
                "targetSum": 22
            },
            "output": [ [5, 4, 11, 2],[5, 8, 4, 5] ]
        },
        {
            "input": { "items": [1, 2, 3], "targetSum": 5 },
            "output": []
        }           
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["items"]),
            targetSum=case["input"]["targetSum"]
        )
