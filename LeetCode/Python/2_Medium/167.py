# [ LeetCode ] 167. Two Sum II - Input Array Is Sorted

def solution(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers)-1
    while left < right:
        sum_of_two_numbers: int = numbers[left] + numbers[right]
        if sum_of_two_numbers == target:
            return [left+1, right+1]
        elif sum_of_two_numbers > target:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int]] | list[int]] = [
        {
            "input": {
                "numbers": [2, 7, 11, 15],
                "target": 9
            },
            "output": [1, 2]
        },
        {
            "input": {
                "numbers": [2, 3, 4],
                "target": 6
            },
            "output": [1, 3]
        },
        {
            "input": {
                "numbers": [-1, 0],
                "target": -1
            },
            "output": [1, 2]
        },                
    ]
    for case in cases:
        assert case["output"] == solution(
            numbers=case["input"]["numbers"], target=case["input"]["target"]
        )
        