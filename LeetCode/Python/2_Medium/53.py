# [ LeetCode ] 53. Maximum Subarray

def solution(nums: list[int]) -> int:
    answer: int = nums[0]
    current_sum: int = 0
    for number in nums:
        current_sum = max(current_sum, 0)
        current_sum += number
        answer = max(answer, current_sum)
    
    return answer


if __name__ == "__main__":
    cases: list[str, dict[str, list[int]] | int] = [
        {
            "input": {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]},
            "output": 6
        },
        {
            "input": {"nums": [1]},
            "output": 1
        },
        {
            "input": {"nums": [5, 4, -1, 7, 8]},
            "output": 23
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        