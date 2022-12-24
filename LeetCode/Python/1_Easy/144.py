# [ LeetCode ] 144. Binary Tree Preorder Traversal

def solution(root: "TreeNode") -> list[int]:
    def preorder_traverse(node: TreeNode) -> None:
        nonlocal answer
        if node:
            answer.append(node.val)
            
            if node.left:
                preorder_traverse(node=node.left)
            if node.right:
                preorder_traverse(node=node.right)
    
    
    answer: list[int] = []
    preorder_traverse(node=root)
    return answer


def another_solution(root: "TreeNode") -> list[int]:
    answer: list[int] = []
        
    if root:
        stack: list[TreeNode] = [root]
        while stack:
            count: int = len(stack)
            while count:
                node: TreeNode = stack.pop()
                answer.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                count -= 1
                    
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
            "output": [1, 2, 3]
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
        assert case["output"] == another_solution(
            root=create_binary_tree(index=0, items=case["input"]["items"])
        )        
        