# [ LeetCode ] 88. Merge Sorted Array

def solution(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    m, n = len(nums1) - len(nums2), len(nums2)
    for i in range(n):
        nums1[m+i], nums2[i] = nums2[i], nums1[m+i]
    
    nums1.sort()
    
    return nums1


def another_solution(
    nums1: list[int], m: int, nums2: list[int], n: int
) -> list[int]:
    pass


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | list[int]]] = [
        {
            "input": {
                "nums1": [1, 2, 3, 0, 0, 0],
                "m": 3,
                "nums2": [2, 5, 6],
                "n": 3
            },
            "output": [1, 2, 2, 3, 5, 6]
        },
        {
            "input": {
                "nums1": [1],
                "m": 1,
                "nums2": [],
                "n": 0
            },
            "output": [1]
        },
        {
            "input": {
                "nums1":  [0],
                "m": 0,
                "nums2": [1],
                "n": 1
            },
            "output": [1]
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
