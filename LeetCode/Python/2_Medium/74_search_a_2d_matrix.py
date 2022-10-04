# [ LeetCode ] 74. Search a 2D Matrix

def solution(matrix: list[list[int]], target: int) -> bool:
    M, N = len(matrix), len(matrix[0])
    left, right = 0, M - 1
    while left <= (N - 1) and right >= 0:
        compare: int = matrix[right][left]
        if compare > target:
            right -= 1
        elif compare < target:
            left += 1
        else:
            return True

    return False


def another_solution(matrix: list[list[int]], target: int) -> bool:
    M, N = len(matrix), len(matrix[0])
    start, end = 0, M * N - 1
    while start <= end:
        middle: int = start + (end - start) // 2
        compare: int = matrix[middle//N][middle%N]
        if compare > target:
            end = middle - 1
        elif compare < target:
            start = middle + 1
        else:
            return True
        
    return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]] | int] | bool]] = [
        {
            "input": {
                "matrix": [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]
                ],
                "target": 3
            },
            "output": True
        },
        {
            "input": {
                "matrix": [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]                    
                ],
                "target": 13
            },
            "output": False
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        