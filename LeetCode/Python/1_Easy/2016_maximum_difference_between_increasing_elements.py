# [ LeetCode ] 2016. Maximum Difference Between Increasing Elements

def solution(nums: list[int]) -> int:
    answer: int = 0
    minimum: int = nums[0]
    for idx in range(1, len(nums)):
        if nums[idx] < minimum:
            minimum = nums[idx]
        elif (nums[idx] - minimum) > answer:
            answer = nums[idx] - minimum
    
    return -1 if answer == 0 else answer
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "nums": [7, 1, 5, 4] },
            "output": 4
        },
        {
            "input": { "nums": [9, 4, 3, 2] },
            "output": -1
        },
        {
            "input": { "nums": [1, 5, 2, 10] },
            "output": 9
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        