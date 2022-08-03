# [ LeetCode ] 704. Binary Search


def solution(nums: list[int], target: int) -> int:
    start, end = 0, len(nums)-1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    
    return -1
    

def another_solution(nums: list[int], target: int) -> int:
    from bisect import bisect_left, bisect_right
    return (
        bisect_right(nums, target) - 1 
        if bisect_right(nums, target) != bisect_left(nums, target)
        else -1
    )
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | int]] = [
        {
            "input": {
                "nums": [-1, 0, 3, 5, 9, 12],
                "target": 9
            },
            "output": 4
        },
        {
            "input": {
                "nums": [-1, 0, 3, 5, 9, 12],
                "target": 2
            },
            "output": -1
        }        
    ]
    for case in cases:
        assert case["output"] == solution(
            nums=case["input"]["nums"], target=case["input"]["target"]
        )
        assert case["output"] == another_solution(
            nums=case["input"]["nums"], target=case["input"]["target"]
        )        
    