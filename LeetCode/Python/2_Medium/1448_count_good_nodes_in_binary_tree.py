# [ LeetCode ] 1448. Count Good Nodes in Binary Tree

def solution(root: "TreeNode") -> int:
    def preorder_traversal(maximum_number: int, node: "TreeNode") -> None:
        nonlocal answer    
        if node:
            if node.val >= maximum_number:
                answer += 1
                maximum_number = node.val
            
            preorder_traversal(
                maximum_number=maximum_number,
                node=node.left
            )
            preorder_traversal(
                maximum_number=maximum_number,
                node=node.right
            )

    answer: int = 0
    maximum_number: int = (-10 ** 4 - 1)
    preorder_traversal(maximum_number=maximum_number, node=root)
        
    return answer


def another_solution(root: "TreeNode") -> int:
    from collections import deque
    
    
    answer: int = 0
    queue: deque = deque()
    queue.append((root, root.val))
    
    while queue:
        node, maximum_number = queue.popleft()
        if node.val >= maximum_number:
            answer += 1
            maximum_number = node.val
        
        if node.left:
            queue.append((node.left, maximum_number))
        
        if node.right:
            queue.append((node.right, maximum_number))

    return answer


if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val, left= None, right= None) -> None:
            self.val = val
            self.left = left
            self.right = right
    
    
    def create_binary_tree(index: int, items: list[int]) -> TreeNode:
        N: int = len(items)
        if items[index]:
            root: TreeNode = TreeNode(val=items[index])
            if index * 2 + 1 < N:
                root.left = create_binary_tree(
                    index=index * 2 + 1, items=items
                )
            
            if index * 2 + 2 < N:
                root.right = create_binary_tree(
                    index=index * 2 + 2, items=items
                )
            
            return root

        else:
            return None
    
    
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": {
                "TreeNode": [3, 1, 4, 3, None, 1, 5]
            },
            "output": 4
        },
        {
            "input": {
                "TreeNode": [3, 3, None, 4, 2]
            },
            "output": 3
        },
        {
            "input": {
                "TreeNode": [1]
            },
            "output": 1
        },        
        {
            "input": {
                "TreeNode": [
                    -1, 5, -2, 4, 4, 2, -2, None, None, -4, None, -2, 3,
                    None, -2, 0, None, -1, None, -3, None, -4, -3, 3, None,
                    None, None, None, None, None, None, 3, -3
                ]
            },
            "output": 5
        }                
    ]
    for case in cases:
        root: TreeNode = create_binary_tree(
            index=0, items=case["input"]["TreeNode"]
        )
        assert case["output"] == solution(root=root)
        assert case["output"] == another_solution(root=root)
            