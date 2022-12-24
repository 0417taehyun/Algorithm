# [ LeetCode ] 112. Path Sum

def solution(root: "TreeNode", targetSum: int) -> bool:
    def inorder_traverse(current_sum: int, node: TreeNode) -> None:
        nonlocal answer
        if node:
            current_sum += node.val
            
            if node.left or node.right:
                if node.left:
                    inorder_traverse(current_sum=current_sum, node=node.left)
                if node.right:
                    inorder_traverse(current_sum=current_sum, node=node.right)
            
            else:
                if current_sum == targetSum:
                    answer += 1
                
                
    answer: int = 0
    inorder_traverse(current_sum=0, node=root)
    return answer > 0
    

def dfs_solution(root: "TreeNode", targetSum: int) -> bool:
    if root:
        stack: list[list[TreeNode, int]] = [[root, targetSum-root.val]]
        while stack:
            node, current_sum = stack.pop()
            if node.left or node.right:
                if node.right:
                    stack.append([node.right, current_sum-node.right.val])
                if node.left:
                    stack.append([node.left, current_sum-node.left.val])
                    
            elif current_sum == 0:
                return True
            
        return False


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
                    5, 4, 8, 11, None, 13, 4, 7, 2,  None, None, None, 1
                ],
                "targetSum": 22
            },
            "output": True
        },
        {
            "input": { "items": [1, 2, 3], "targetSum": 5 },
            "output": False
        }        
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["items"]),
            targetSum=case["input"]["targetSum"]
        )
        assert case["output"] == dfs_solution(
            root=create_binary_tree(index=0, items=case["input"]["items"]),
            targetSum=case["input"]["targetSum"]
        )    
    