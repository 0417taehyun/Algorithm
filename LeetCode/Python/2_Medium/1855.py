# [ LeetCode ] 1855. Maximum Distance Between a Pair of Values

def solution(nums1: list[int], nums2: list[int]) -> int:
    answer: int = 0
    left, right = len(nums1) - 1, len(nums2) - 1
    while left >= 0 and right >= 0:
        if left > right:
            left -= 1
        elif nums1[left] > nums2[right]:
            right -= 1
        else:
            answer = max(answer, right - left)
            left -= 1
    
    return answer


def another_solution(nums1: list[int], nums2: list[int]) -> int:
    answer: int = 0
    for i, number in enumerate(nums1):
        start, end = i, len(nums2) - 1
        while start <= end:
            middle: int = start + (end - start) // 2
            if number <= nums2[middle]:
                start = middle + 1
            else:
                end = middle - 1
        
        answer = max(answer, end - i)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": {
                "nums1": [55, 30, 5, 4, 2],
                "nums2": [100, 20, 10, 10, 5]
            },
            "output": 2
        },
        {
            "input": {
                "nums1": [2, 2, 2],
                "nums2": [10, 10, 1]
            },
            "output": 1
        },
        {
            "input": {
                "nums1": [30, 29, 19, 5],
                "nums2": [25, 25, 25, 25, 25]
            },
            "output": 2
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
