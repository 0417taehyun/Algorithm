# [ LeetCode ] 268. Missing Number

def solution(nums: list[int]) -> int:
    answer: int = 0
    for index, number in enumerate(nums, start=1):
        answer ^= (number ^ index)
    return answer


def another_solution(nums: list[int]) -> int:
    expected_sum: int = len(nums) * (len(nums) + 1) // 2
    actual_sum: int = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {"input": {"nums": [3, 0, 1]}, "output": 2},
        {"input": {"nums": [1, 0]}, "output": 2},
        {"input": {"nums": [6, 4, 2, 5, 0, 1]}, "output": 3},
        {"input": {"nums": [6, 4, 2, 5, 3, 1]}, "output": 0}
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        