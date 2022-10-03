# [ LeetCode ] 1608. Special Array With X Elements Greater Than or Equal X

def solution(nums: list[int]) -> int:
    start, end = 0, max(nums)
    while start <= end:
        count: int = 0
        middle: int = start + (end - start) // 2
        for num in nums:
            if num >= middle:
                count += 1
        
        if middle > count:
            end = middle - 1
        elif middle < count:
            start = middle + 1
        else:
            return middle
    
    return -1
        

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": {"nums": [3, 5]},
            "output": 2
        },
        {
            "input": {"nums": [0, 0]},
            "output": -1
        },
        {
            "input": {"nums": [0, 4, 3, 0, 4]},
            "output": 3
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        