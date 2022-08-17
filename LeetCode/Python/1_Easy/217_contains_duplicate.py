# [ LeetCode ] 217. Contains Duplicate

def solution(nums: list[int]) -> bool:
    seen: set = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    
    return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | bool]] = [
        {
            "input": { "nums": [1, 2, 3, 1] },
            "output": True
        },
        {
            "input": { "nums": [1, 2, 3, 4] },
            "output": False
        },
        {
            "input": { "nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] },
            "output": True
        }                
    ]
    for case in cases:
        assert case["output"] == solution(nums=case["input"]["nums"])
    