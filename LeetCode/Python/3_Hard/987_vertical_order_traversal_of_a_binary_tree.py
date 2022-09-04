# [ LeetCode ] 987. Vertical Order Traversal of a Binary Tree

def solution(root: "TreeNode") -> list[list[int]]:
    def inorder_traverse(row: int, column: int, node: TreeNode) -> None:
        nonlocal trees
        if node:
            if node.left:
                inorder_traverse(row=row+1, column=column-1, node=node.left)
            
            if column in trees:
                if row in trees[column]:
                    trees[column][row].append(node.val)
                else:
                    trees[column][row] = [node.val]
            
            else:
                trees[column] = {row: [node.val]}
            
            if node.right:
                inorder_traverse(row=row+1, column=column+1, node=node.right)

    
    answer: list[list[int]] = []
    trees: dict[int, dict[int, list[list[int]]]] = {}
    inorder_traverse(row=0, column=0, node=root)
    for _, nested_nodes in sorted(trees.items()):
        temp: list[int] = []
        for _, nodes in sorted(nested_nodes.items()):
            temp.extend(sorted(nodes))
        answer.append(temp)
    return answer


def another_solution(root: "TreeNode") -> list[list[int]]:
    pass


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int | None]] | list[list[int]]]] = [
        {
            "input": {
                "nodes": [3, 9, 20, None, None, 15, 7]
            },
            "output": [[9],[3, 15],[20],[7]]
        },
        {
            "input": {
                "nodes": [1, 2, 3, 4, 5, 6, 7]
            },
            "output": [[4],[2],[1, 5, 6],[3],[7]]
        },
        {
            "input": {
                "nodes": [1, 2, 3, 4, 6, 5, 7]
            },
            "output": [[4],[2],[1, 5, 6],[3],[7]]
        },
        {
            "input": {
                "nodes": [3, 1, 4, 0, 2, 2]
            },
            "output": [[0],[1],[3, 2, 2],[4]]
        }                            
    ]
    
    
    class TreeNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
    
    
    def create_binary_tree(index: int, items: list[int | None]) -> TreeNode:
        if items[index] != None:
            root: TreeNode = TreeNode(val=items[index])
        
            if (index*2+1) < len(items):
                root.left = create_binary_tree(index=index*2+1, items=items)
            if (index*2+2) < len(items):
                root.right = create_binary_tree(index=index*2+2, items=items)
            
            return root

        else:
            return None
        
    
    for case in cases:
        assert case["output"] == solution(
            root=create_binary_tree(index=0, items=case["input"]["nodes"])
        )
        