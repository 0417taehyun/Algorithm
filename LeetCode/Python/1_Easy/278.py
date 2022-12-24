# [ LeetCode ] 278. First Bad Version

def isBadVersion(version: int) -> bool:
    """
    pre-defined API
    """
    if version >= 4:
        return True
    else:
        return False


def solution(n: int) -> int:
    start, end, answer = 1, n, 0
    while start <= end:
        middle = (start + end) // 2
        if isBadVersion(middle):
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    return answer


def another_solution(n: int) -> int:
    start, end = 1, n
    while start <= end:
        middle: int = start + (end - start) // 2
        if isBadVersion(version=middle):
            end = middle - 1
        else:
            start = middle + 1
    
    return start
    

if __name__ == "__main__":
    case: dict[str, dict[str, int] | int] = {
        "input": {"n": 5},
        "output": 4
    }
    assert case["output"] == solution(**case["input"])
    assert case["output"] == another_solution(**case["input"])
    