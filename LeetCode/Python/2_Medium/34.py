# [ LeetCode ] 34. Find First and Last Position of Element in Sorted Array

def solution(nums: list[int], target: int) -> list[int]:    
    answer: list[int] = []
    is_exist: bool = False
    
    start, end = 0, len(nums) - 1
    while start <= end:
        middle: int = start + (end - start) // 2
        compare: int = nums[middle]
        if compare < target:
            start = middle + 1
        elif compare > target:
            end = middle - 1
        else:
            is_exist = True
            end = middle - 1
    
    if is_exist:
        answer.append(start)
    else:
        answer.append(-1)
        
    
    start, end = 0, len(nums) - 1
    while start <= end:
        middle: int = start + (end - start) // 2
        compare: int = nums[middle]
        if compare > target:
            end = middle - 1
        elif compare < target:
            start = middle + 1
        else:
            is_exist = True
            start = middle + 1
            
    if is_exist:
        answer.append(end)
    else:
        answer.append(-1)
    
    return answer


def another_soluion(nums: list[int], target: int) -> list[int]:
    def find_index(nums: list[int], target: int, is_from_left: bool) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle: int = start + (end - start) // 2
            compare: int = nums[middle]
            if compare > target:
                end = middle - 1
            elif compare < target:
                start = middle + 1
            else:
                if is_from_left:
                    if middle == start or nums[middle - 1] < target:
                        return middle
                    else:
                        end = middle - 1
            
                else:
                    if middle == end or nums[middle + 1] > target:
                        return middle
                    else:
                        start = middle + 1
                        
            return -1
        
        
        left_index: int = find_index(
            nums=nums, target=target, is_from_left=True
        )
        if left_index == -1:
            return [-1, -1]
        else:
            right_index: int = find_index(
                nums=nums, target=target, is_from_left=False
            )
            return [left_index, right_index]


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | list[int]]] = [
        {
            "input": {
                "nums": [5, 7, 7, 8, 8, 10],
                "target": 8
            },
            "output": [3, 4]
        },
        {
            "input": {
                "nums": [5, 7, 7, 8, 8, 10],
                "target": 6
            },
            "output": [-1, -1]
        },
        {
            "input": {
                "nums": [],
                "target": 0
            },
            "output": [-1, -1]
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        