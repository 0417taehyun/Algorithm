# [ LeetCode ] 367. Valid Perfect Square

def solution(num: int) -> bool:
    if num == 1:
        return True
    else:
        start, end = 1, num // 2
        while start <= end:
            middle: int = (start + end) // 2
            target: int = middle * middle
            
            if target > num:
                end = middle - 1
            elif target < num:
                start = middle + 1
            else:
                return True

        return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | bool]] = [
        { "input": { "num": 16 }, "output": True },
        { "input": { "num": 14 }, "output": False },
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
    