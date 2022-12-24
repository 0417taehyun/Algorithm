# [ LeetCode ] 35. Search Insert Position

def solution(nums: list[int], target: int) -> int:
    start, end, answer = 0, len(nums)-1, 0
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            answer = middle
            end = middle - 1
        else:
            answer = middle + 1
            start = middle + 1
    
    return answer


def another_solution(nums: list[int], target: int) -> int:
    from bisect import bisect_left; return bisect_left(nums, target)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | int]] = [
        {
            "input": {
                "nums": [1, 3, 5, 6],
                "target": 5
            },
            "output": 2
        },
        {
            "input": {
                "nums": [1, 3, 5, 6],
                "target": 2
            },
            "output": 1
        },
        {
            "input": {
                "nums": [1, 3, 5, 6],
                "target": 7
            },
            "output": 4
        }                
    ]
    for case in cases:
        assert case["output"] == solution(
            nums=case["input"]["nums"], target=case["input"]["target"]
        )
        assert case["output"] == another_solution(
            nums=case["input"]["nums"], target=case["input"]["target"]
        )
                