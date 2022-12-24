# [ LeetCode ] 349. Intersection of Two Arrays

def solution(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) < len(nums2):
        return solution(nums1=nums2, nums2=nums1)
    else:
        numbers: dict[int, int] = {}
        for number in nums1:
            if not number in numbers:
                numbers[number] = 1

        answer: list[int] = []
        for number in nums2:
            if number in numbers:
                answer.append(number)
                numbers.pop(number)

        return answer

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | list[int]]] = [
        {
            "input": {
                "nums1": [1, 2, 2, 1],
                "nums2": [2, 2]
            },
            "output": [2]
        },
        {
            "input": {
                "nums1": [4, 9, 5],
                "nums2": [9, 4, 9, 8, 2]
            },
            "output": [4, 9]
        },
        {
            "input": {
                "nums1": [1, 3, 4],
                "nums2": [2, 5]
            },
            "output": []
        }                 
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
            