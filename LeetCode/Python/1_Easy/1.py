# [ LeetCode ] 1. Two Sum

def solution(nums: list[int], target: int) -> list[int]:
    table: dict[int, int] = {
        index: number for index, number in enumerate(nums)
    }
    numbers: list[tuple[int, int]] = sorted(table.items(), key=lambda x: x[1])
    left, right = 0, len(nums) - 1
    while left < right:
        left_value, right_value = numbers[left][1], numbers[right][1]
        compare: int = left_value + right_value
            
        if compare > target:
            right -= 1
        elif compare < target:
            left += 1
        else:
            return [numbers[left][0], numbers[right][0]]


def another_solution(nums: list[int], target: int) -> list[int]:
    numbers: dict[int, int] = {
        number: index for index, number in enumerate(nums)
    }
    for index, number in enumerate(nums):
        diff: int = target - number
        if diff in numbers and numbers[diff] != index:
            return [index, numbers[diff]]


def one_pass_solution(nums: list[int], target: int) -> list[int]:
    numbers: dict[int, int] = {}
    for index, number in enumerate(nums):
        diff: int = target - number
        if diff in numbers:
            return [numbers[diff], index]
        
        else:
            numbers[number] = index

    
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
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == one_pass_solution(**case["input"])
                