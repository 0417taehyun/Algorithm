# [ LeetCode ] 1502. Can Make Arithmetic Progression From Sequence

def solution(arr: list[int]) -> bool:
    arr.sort()
    for idx in range(len(arr) - 2):
        if (arr[idx + 1] - arr[idx]) != (arr[idx + 2] - arr[idx + 1]):
            return False
    
    return True


def another_solution(arr: list[int]) -> bool:
    minimum_number, maximum_number = min(arr), max(arr)
    diff: float = (maximum_number - minimum_number) / (len(arr) - 1)
    if diff == int(diff):
        diff: int = int(diff)
    else:
        return False
    
    index: int = 0
    while index < len(arr):
        if arr[index] == (minimum_number + (index * diff)):
            index += 1
        else:
            distance: int = arr[index] - minimum_number
            if distance % diff == 0:
                target: int = distance // diff
                if arr[index] == arr[target]:
                    return False
                else:
                    arr[index], arr[target] = arr[target], arr[index]
            
            else:
                return False
    
    return True    


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | bool]] = [
        {
            "input": {"arr": [3, 5, 1]},
            "output": True
        },
        {
            "input": {"arr": [4, 2, 1]},
            "output": False
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
    