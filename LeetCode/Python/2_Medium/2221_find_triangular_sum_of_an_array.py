# [ LeetCode ] 2221. Find Triangular Sum of an Array

def solution(nums: list[int]) -> int:
    answer: int = 0
    while nums:
        for index in range(len(nums) - 1):
            nums[index] = (nums[index] + nums[index + 1]) % 10
        
        answer = nums.pop()
        
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "nums": [1,2,3,4,5] },
            "output": 8
        },
        {
            "input": { "nums": [5] },
            "output": 5
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        