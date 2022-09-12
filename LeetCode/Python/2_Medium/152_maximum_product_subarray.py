# [ LeetCode ] 152. Maximum Product Subarray

def solution(nums: list[int]) -> int:
    answer: int = nums[0]
    max_product, min_product = nums[0], nums[0]
    for idx in range(1, len(nums)):
        max_product, min_product = (
            max(nums[idx], max_product*nums[idx], min_product*nums[idx]),
            min(nums[idx], max_product*nums[idx], min_product*nums[idx])
        )
        answer = max(max_product, answer)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": {"nums": [2, 3, -2, 4]},
            "output": 6
        },
        {
            "input": {"nums": [-2, 0, -1]},
            "output": 0
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        