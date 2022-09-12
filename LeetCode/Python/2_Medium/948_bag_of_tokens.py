# [ LeetCode ] 948. Bag of Tokens

def solution(tokens: list[int], power: int) -> int:
    from collections import deque
    
    
    answer: int = 0
    queue: deque = deque(sorted(tokens))
    while queue:
        target: int = queue.popleft()
        if target <= power:
            answer += 1
            power -= target
        else:
            if len(queue) <= 1 or answer == 0:
                break
            else:
                power += (queue.pop() - target)
    
    return answer


def another_solution(tokens: list[int], power: int) -> int:
    tokens.sort()
    answer, left, right = 0, 0, len(tokens) - 1
    while left <= right:
        target: int = tokens[left]
        if target <= power:
            answer += 1
            power -= target
            left += 1
        elif answer > 0:
            power += (tokens[right] - target)
            left += 1                    
            right -= 1
        else:
            break
    
    return answer
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | int]] = [
        {
            "input": { "tokens": [100], "power": 50 },
            "output": 0
        },
        {
            "input": { "tokens": [100, 200], "power": 150 },
            "output": 1
        },
        {
            "input": { "tokens": [100, 200, 300, 400], "power": 200 },
            "output": 2
        },
        {
            "input": { "tokens": [55, 71, 82], "power": 54 },
            "output": 0
        }                        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        