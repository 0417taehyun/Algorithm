# [ LeetCode ] 350. Intersection of Two Arrays II

def solution(nums1: list[int], nums2: list[int]) -> list[int]:
    def create_hash_map(nums: list[int]) -> dict[int, int]:
        numbers: dict[int, int] = {}
        for number in nums:
            if number in numbers:
                numbers[number] += 1
            else:
                numbers[number] = 1
        
        return numbers
    
    
    def find_intersection(
        numbers: dict[int, int], compare: list[int]
    ) -> list[int]:
        answer: list[int] = []
        for number in compare:
            if number in numbers and numbers[number] > 0:
                answer.append(number)
                numbers[number] -= 1
        
        return answer
    
    
    if len(nums1) <= len(nums2):
        numbers: dict[int, int] = create_hash_map(nums=nums2)
        answer: list[int] = find_intersection(numbers=numbers, compare=nums1)
    
    else:
        numbers: dict[int, int] = create_hash_map(nums=nums1)
        answer: list[int] = find_intersection(numbers=numbers, compare=nums2)
    
    return answer


def another_solution(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()
    
    answer: list[int] = []
    left, right = 0, 0
    while left < len(nums1) and right < len(nums2):
        left_number, right_number = nums1[left], nums2[right]
        if left_number > right_number:
            right += 1
        elif left_number < right_number:
            left += 1
        else:
            answer.append(left_number)
            left += 1
            right += 1
    
    return answer
                    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | list[int]]] = [
        {
            "input": {
                "nums1": [1, 2, 2, 1],
                "nums2": [2, 2]
            },
            "output": [2, 2]
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
        assert case["output"] == another_solution(**case["input"])
        