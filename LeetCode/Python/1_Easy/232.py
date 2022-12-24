# [ LeetCode ] 232. Implement Queue using Stacks

from collections import deque


class Solution:
    def __init__(self):
        self.dequeue: deque = deque()

    def push(self, x: int) -> None:
        self.dequeue.append(x)

    def pop(self) -> int:
        return self.dequeue.popleft()

    def peek(self) -> int:
        return self.dequeue[0]

    def empty(self) -> bool:
        return len(self.dequeue) == 0


class AnotherSolution:
    def __init__(self) -> None:
        self.s1: list[int] = []
        self.s2: list[int] = []

    def push(self, x: int) -> None:
        self.s1.append(x)
    
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        return self.s2.pop()
    
    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        
        else:
            return self.s1[0]
    
    def empty(self) -> bool:
        return self.s1 == [] and self.s2 == []
    

if __name__ == "__main__":
    case: dict[str, list[str] | list[list[int]] | list[list[int] | bool]] = {
        "input": {
            "operations": ["MyQueue", "push", "push", "peek", "pop", "empty"],
            "data": [[], [1], [2], [], [], []]
        },
        "output": [None, None, None, [1], [1], False]
    }
    solution_result: list[list[int] | bool] = [None]
    another_solution_result: list[list[int] | bool] = [None]
    for operation, data in zip(
        case["input"]["operations"], case["input"]["data"]
    ):
        if operation == "MyQueue":
            solution = Solution()
            another_solution = AnotherSolution()
        
        elif operation == "push":
            solution_result.append(solution.push(x=data))
            another_solution_result.append(another_solution.push(x=data))
        
        elif operation == "peek":
            solution_result.append(solution.peek())
            another_solution_result.append(another_solution.peek())
            
        elif operation == "pop":
            solution_result.append(solution.pop())
            another_solution_result.append(another_solution.pop())
        
        elif operation == "empty":
            solution_result.append(solution.empty())
            another_solution_result.append(another_solution.empty())
    
    assert case["output"] == solution_result
    assert case["output"] == another_solution_result
        