# [ LeetCode ] 255. Verify Preorder Sequence in Binary Search Tree

def solution(preorder: list[int]) -> bool:
    stack: list[int] = []
    low: int = 0
    for value in preorder:
        if value < low:
            return False
        while stack and value > stack[-1]:
            low = stack.pop()
        stack.append(value)
    return True
    