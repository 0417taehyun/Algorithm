# [ LeetCode ] 976. Largest Perimeter Triangle

def solution(nums: list[int]) -> int:
    nums.sort(reverse=True)
    for idx in range(len(nums)-2):
        a, b, c = nums[idx], nums[idx+1], nums[idx+2]
        if a < (b + c):
            return a + b + c
    return 0


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": {"nums": [2, 1, 2]},
            "output": 5
        },
        {
            "input": {"nums": [1, 2, 1]},
            "output": 0
        }        
    ]
    for case in cases:
        assert case["output"] == solution(nums=case["input"]["nums"])
    