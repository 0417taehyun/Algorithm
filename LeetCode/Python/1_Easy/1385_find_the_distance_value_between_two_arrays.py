# [ LeetCode ] 1385. Find the Distance Value Between Two Arrays

def solution(arr1: list[int], arr2: list[int], d: int) -> int:
    def binary_search(start: int, end: int, position: int) -> bool:
        while start <= end:
            middle: int = start + (end - start) // 2
            target: int = arr2[middle]
            
            if abs(target - position) <= d:
                return False
            elif target > position:
                end = middle - 1
            else:
                start = middle + 1
        
        return True
            
    
    arr2.sort()
    answer, start, end = 0, 0, len(arr2) - 1
    for position in arr1:
        if binary_search(start=start, end=end, position=position):
            answer += 1
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[list[int] | int] | int]] = [
        {
            "input": {
                "arr1": [1, 4, 2, 3],
                "arr2": [-4, -3, 6, 10, 20, 30],
                "d": 3
            },
            "output": 2
        },
        {
            "input": {
                "arr1": [2, 1, 100, 3],
                "arr2": [-5, -2, 10, -3, 7],
                "d": 6
            },
            "output": 1
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
