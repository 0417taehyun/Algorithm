# [ LeetCode ] 637. Average of Levels in Binary Tree

def solution(root: "TreeNode") -> list[float]:
    def traverse(depth: int, node: TreeNode) -> None:
        nonlocal tree
        if node:
            if depth in tree:
                tree[depth].append(node.val)
            else:
                tree[depth] = [node.val]
            
            traverse(depth=depth+1, node=node.left)
            traverse(depth=depth+1, node=node.right)

    
    tree: dict[int, int] = {}
    traverse(depth=0, node=root)
    
    answer: list[float] = [ 0 for _ in range(len(tree)) ]
    for index, value in tree.items():
        answer[index] = sum(value) / len(value)
    
    return answer
    

def another_solution(root: "TreeNode") -> list[float]:
    from collections import deque
    
    
    queue: deque = deque([root])
    answer: list[float] = []
    while queue:
        same_level_count = same_level_length = len(queue)
        same_level_sum: int = 0
        
        while same_level_count > 0:
            node: TreeNode = queue.popleft()            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
                
            same_level_sum += node.val
            same_level_count -= 1
        
        answer.append(same_level_sum / same_level_length)
        
    return answer
    
    
if __name__ == "__main__":    
    class TreeNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
    
    
    def create_binary_tree(index: int, items: list[int]) -> TreeNode | None:
        if items[index]:
            node: TreeNode = TreeNode(val=items[index])
        
            if (index * 2 + 1) < len(items):
                node.left = create_binary_tree(index=index*2+1, items=items)
            
            if (index * 2 + 2) < len(items):
                node.right = create_binary_tree(index=index*2+2, items=items)
            
            
            return node

        else:
            return None
    
    
    cases: list[dict[str, dict[str, list[int]] | list[float]]] = [
        {
            "input": { "tree": [3, 9, 20, None, None, 15, 7] },
            "output": [3.00000, 14.50000, 11.00000]
        },
        {
            "input": { "tree": [3, 9, 20, 15, 7] },
            "output": [3.00000, 14.50000, 11.00000]
        }         
    ]
    for case in cases:     
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["tree"])
        )
        assert case["output"] == another_solution(
            root=create_binary_tree(index=0, items=case["input"]["tree"])
        )        
    