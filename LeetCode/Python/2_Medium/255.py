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


def another_solution(preorder: list[int]) -> bool:
    low: int = 0
    index: int = 0
    for node in preorder:
        if node < low:
            return False
        while index > 0 and node > preorder[index-1]:
            low = preorder[index-1]
            index -= 1
        preorder[index] = node
        index += 1
    return True
