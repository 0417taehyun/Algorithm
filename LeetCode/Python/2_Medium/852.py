# [ LeetCode ] 852. Peak Index in a Mountain Array

def solution(arr: list[int]) -> int:
    start, end = 0, len(arr) - 1
    while start <= end:
        middle: int = (start + end) // 2
        target, previous, next = arr[middle], arr[middle-1], arr[middle+1]
        
        if target < previous:
            end = middle
        elif target < next:
            start = middle
        else:
            return middle


def another_solution(arr: list[int]) -> int:
    start, end = 0, len(arr) - 1
    while start < end:
        middle: int = (start + end) // 2
        target, next_value = arr[middle], arr[middle+1]
        if target < next_value:
            start = middle + 1
        else:
            end = middle

    return start
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "arr": [0, 1, 0] },
            "output": 1
        },
        {
            "input": { "arr": [0, 2, 1, 0] },
            "output": 1
        },
        {
            "input": { "arr": [0, 10, 5, 2] },
            "output": 1
        },
        {
            "input": { "arr": [3, 9, 8, 6, 4] },
            "output": 1
        }                       
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])