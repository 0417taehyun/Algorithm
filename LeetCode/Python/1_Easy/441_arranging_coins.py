# [ LeetCode ] 441. Arranging Coins

def solution(n: int) -> int:
    stair: int = 1
    while n >= stair:
        n -= stair
        stair += 1
    return stair - 1


def another_solution(n: int) -> int:
    start, end = 1, n
    while start <= end:
        middle: int = start + (end - start) // 2
        stair: int = (middle * (middle + 1)) // 2
        if stair <= n:
            start = middle + 1
        else:
            end = middle - 1
    
    return end


def math_solution(n: int) -> int:
    return int((2*n+0.25)**0.5-0.5)
 

if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        { "input": { "n": 5 }, "output": 2 },
        { "input": { "n": 8 }, "output": 3 }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        