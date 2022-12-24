# [ LeetCode ] 1822. Sign of the Product of an Array

def solution(nums: list[int]) -> int:
    answer: int = 1
    for number in nums:
        if number == 0:
            return 0
        elif number < 0:
            answer *= -1
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": {"nums": [-1, -2, -3, -4, 3, 2, 1]},
            "output": 1
        },
        {
            "input": {"nums": [1, 5, 0, 2, -3]},
            "output": 0
        },
        {
            "input": {"nums": [-1, 1, -1, 1, -1]},
            "output": -1
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        