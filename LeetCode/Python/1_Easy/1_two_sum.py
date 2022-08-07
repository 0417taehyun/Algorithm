# [ LeetCode ] 1. Two Sum

def solution(nums: list[int], target: int) -> list[int]:
    numbers: list[tuple[int, int]] = sorted(
        [ (idx, number) for idx, number in enumerate(nums) ],
        key=lambda x: x[1]
    )
    left, right = 0, len(nums) - 1
    while left <= right:
        compare_target: int = numbers[left][1] + numbers[right][1]
        if compare_target == target:
            return [ numbers[left][0], numbers[right][0] ]
        elif compare_target > target:
            right -= 1
        else:
            left += 1


def another_solution(nums: list[int], target: int) -> list[int]:
    numbers: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement: int = target - num
        if complement in numbers:
            return [ numbers[complement], idx ]
        else:
            numbers[num] = idx
        
    
if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int]] | list[int]] = [
        {
            "input": {
                "nums": [2, 7, 11, 15],
                "target": 9
            },
            "output": [0, 1]
        },
        {
            "input": {
                "nums": [3,2,4],
                "target": 6
            },
            "output": [1, 2]
        },
        {
            "input": {
                "nums": [3, 3],
                "target": 6
            },
            "output": [0, 1]
        },                
    ]
    for case in cases:
        assert case["output"] == solution(
            nums=case["input"]["nums"], target=case["input"]["target"]
        )
        assert case["output"] == another_solution(
            nums=case["input"]["nums"], target=case["input"]["target"]
        )
                