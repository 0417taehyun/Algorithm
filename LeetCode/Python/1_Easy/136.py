# [ LeetCode ] 136. Single Number

def solution(nums: list[int]) -> int:
    answer: int = 0
    for number in nums:
        answer ^= number
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "nums": [2, 2, 1] },
            "output": 1
        },
        {
            "input": { "nums": [4, 1, 2, 1, 2] },
            "output": 4
        },
                {
            "input": { "nums": [1] },
            "output": 1
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        