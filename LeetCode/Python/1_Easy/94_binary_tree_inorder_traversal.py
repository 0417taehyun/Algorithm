# [ LeetCode ] 94. Binary Tree Inorder Traversal

def solution(root: "TreeNode") -> list[int]:
    def inorder_traverse(node: TreeNode) -> None:
        nonlocal answer
        if node: 
            if node.left:
                inorder_traverse(node=node.left)
            
            answer.append(node.val)
                
            if node.right:
                inorder_traverse(node=node.right)
        
    
    answer: list[int] = []
    inorder_traverse(node=root)
    return answer


def another_solution(root: "TreeNode") -> list[int]:
    answer: list[int] = []
    stack: list[TreeNode] = []
    node: TreeNode = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        answer.append(node.val)
        node = node.right
    
    return answer


def morris_solution(root: "TreeNode") -> list[int]:
    answer: list[int] = []
    current_node: TreeNode = root
    rightmost_node: TreeNode = None
    while current_node:
        if current_node.left:
            rightmost_node = current_node.left
            while rightmost_node.right:
                rightmost_node = rightmost_node.right
            
            temp: TreeNode = current_node
            rightmost_node.right = current_node
            current_node = current_node.left
            temp.left = None
        
        else:
            answer.append(current_node.val)
            current_node = current_node.right
            
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
            "output": [1, 3, 2]
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
        assert case["output"] == morris_solution(
            root=create_binary_tree(index=0, items=case["input"]["items"])
        )                
        