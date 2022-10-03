# [ LeetCode ] 1351. Count Negative Numbers in a Sorted Matrix

def solution(grid: list[list[int]]) -> int:
    answer: int = 0
    
    M, N = len(grid), len(grid[0])
    for i in range(M):
        start, end = 0, N - 1
        while start <= end:
            middle: int = start + (end - start) // 2
            if grid[i][middle] >= 0:
                start = middle + 1
            else:
                end = middle - 1
        
        answer += (N - start)
    
    return answer


def another_solution(grid: list[list[int]]) -> int:
    answer: int = 0
    
    M, N = len(grid), len(grid[0])
    left, right = 0, M - 1
    while left <= (N - 1) and right >= 0:
        if grid[right][left] >= 0:
            left += 1
        else:
            answer += (N - left)
            right -= 1

    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]]] | int]] = [
        {
            "input": {
                "grid": [
                    [4, 3, 2, -1],
                    [3, 2, 1, -1],
                    [1, 1, -1, -2],
                    [-1, -1, -2, -3]
                ]
            },
            "output": 8
        },
        {
            "input": {"grid": [[3, 2], [1, 0]]},
            "output": 0
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        # assert case["output"] == another_solution(**case["input"])
    