# [ LeetCode ] 1457. Pseudo-Palindromic Paths in a Binary Tree

def solution(root: "TreeNode") -> int:
    def preorder_traverse(
        node_val_counts: dict[int, int], node: TreeNode
    ) -> None:
        nonlocal answer
        if node:
            if node.val in node_val_counts:
                node_val_counts[node.val] += 1
            else:
                node_val_counts[node.val] = 1
            
            if node.left or node.right:
                if node.left:
                    preorder_traverse(
                        node_val_counts=node_val_counts.copy(),
                        node=node.left
                    )

                if node.right:
                    preorder_traverse(
                        node_val_counts=node_val_counts.copy(),
                        node=node.right
                    )
            
            else:
                odd_count: int = 0
                for count in node_val_counts.values():
                    if count % 2 != 0:
                        odd_count += 1
                
                if odd_count <= 1:
                    answer += 1
    
    answer: int = 0
    preorder_traverse(node_val_counts={}, node=root)
    return answer


def another_solution(root: "TreeNode") -> int:
    answer: int = 0
    stack: list[tuple[TreeNode, int]] = [(root, 0)]
    while stack:
        node, path = stack.pop()
        if node:
            path ^= (1 << node.val)
            if node.left or node.right:
                stack.append((node.right, path))
                stack.append((node.left, path))
            else:
                if path & (path - 1):
                    answer += 1
    
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
    
    
    def create_binary_tree(items: list[int], index: int) -> TreeNode:
        if items[index] is not None:
            root: TreeNode = TreeNode(val=items[index])
            if (index*2+1) < len(items):
                root.left = create_binary_tree(
                    items=items, index=index*2+1
                )
                
            if (index*2+2) < len(items):
                root.right = create_binary_tree(
                    items=items, index=index*2+2
                )

            return root
            
        else:
            return None
    
    
    cases: list[dict[str, dict[str, list[int | None]] | int]] = [
        {
            "input": { "items": [2, 3, 1, 3, 1, None, 1] },
            "output": 2
        },
        {
            "input": {
                "items": [2, 1, 1, 1, 3, None, None, None, None, None, 1]
            },
            "output": 1
        },
        {
            "input": { "items": [9] },
            "output": 1
        }                
    ]
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(items=case["input"]["items"], index=0)
        )