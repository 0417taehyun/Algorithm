# [ LeetCode ] 153. Find Minimum in Rotated Sorted Array

def solution(nums: list[int]) -> int:
    answer, start, end = 5000, 0, len(nums) - 1
    while start <= end:
        middle: int = start + (end - start) // 2
        if nums[middle] > nums[end]:
            start = middle + 1
        else:
            answer = min(answer, nums[middle])
            end = middle - 1
    
    return answer


def another_solution(nums: list[int]) -> int:
    start, end = 0, len(nums) - 1
    if end == 0:
        return nums[0]
    elif nums[start] < nums[end]:
        return nums[0]
    else:
        while start <= end:
            middle: int = start + (end - start) // 2
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            elif nums[start] > nums[middle]:
                end = middle - 1
            else:
                start = middle + 1


if __name__ == "__main__":
    cases: list[dict[str, dict[list[int]] | int]] = [
        {
            "input": { "nums": [3, 4, 5, 1, 2] },
            "output": 1
        },
        {
            "input": { "nums": [4, 5, 6, 7, 0, 1, 2] },
            "output": 0
        },
        {
            "input": { "nums": [11, 13, 15, 17] },
            "output": 11
        },
        {
            "input": { "nums": [3, 1 ,2] },
            "output": 1
        }                        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        