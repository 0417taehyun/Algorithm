# [ LeetCode ] 33. Search in Rotated Sorted Array

def solution(nums: list[int], target: int) -> int:
    def find_rotate_index(start: int, end: int) -> int:
        if nums[start] < nums[end]:
            return 0 

        else:
            while start <= end:
                middle: int = start + (end - start) // 2
                if nums[middle] > nums[middle + 1]:
                    return middle + 1
                elif nums[middle] < nums[start]:
                    end = middle - 1
                else:
                    start = middle + 1
    
    
    def binary_search(start: int, end: int) -> int:
        while start <= end:
            middle: int = start + (end - start) // 2
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                return middle
        
        return -1
    
    
    n: int = len(nums) - 1
    if n == 0:
        return 0 if nums[0] == target else -1
    else:
        pivot: int = find_rotate_index(start=0, end=n)
        if nums[pivot] == target:
            return pivot
        
        elif pivot == 0:
            return binary_search(start=0, end=n)
        
        elif nums[0] > target:
            return binary_search(start=pivot, end=n)
        
        else:
            return binary_search(start=0, end=pivot)
    
    
def another_solution(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        middle: int = start + (end - start) // 2
        if nums[middle] == target:
            return middle
        
        elif nums[middle] >= nums[start]:
            if nums[start] <= target and nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
                
        else:
            if nums[end] >= target and nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1

    return -1


if __name__ == "__main__":
    cases: list[dict[str, dict[list[int | int]] | int]] = [
        {
            "input": {
                "nums": [4, 5, 6, 7, 0, 1, 2],
                "target": 0
            },
            "output": 4
        },
        {
            "input": {
                "nums": [4, 5, 6, 7, 0, 1, 2],
                "target": 3
            },
            "output": -1
        },
        {
            "input": {
                "nums": [1],
                "target": 0
            },
            "output": -1
        },
        {
            "input": {
                "nums": [1, 3],
                "target": 3
            },
            "output": 1
        },
        {
            "input": {
                "nums": [1, 3],
                "target": 1
            },
            "output": 0
        },
        {
            "input": {
                "nums": [3, 1],
                "target": 3
            },
            "output": 0
        },        
        {
            "input": {
                "nums": [1, 2, 3, 4, 5, 6],
                "target": 4
            },
            "output": 3
        },
        {
            "input": {
                "nums": [4, 5, 6, 7, 8, 1, 2, 3],
                "target": 8
            },
            "output": 4
        }                                              
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
