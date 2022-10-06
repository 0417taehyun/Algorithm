# [ LeetCode ] 633. Sum of Square Numbers

def solution(c: int) -> bool:
    MAX_SQUARE: int = int((2**31 - 1) ** 0.5)
    numbers: set[int] = { number*number for number in range(0, MAX_SQUARE+1) }
    for number in numbers:
        if (c - number) in numbers:
            return True
    return False


def brute_force(c: int) -> bool:
    MAX_SQUARE: int = int(c ** 0.5) + 1
    for a in range(0, MAX_SQUARE):
        for b in range(0, MAX_SQUARE):
            if (a * a) + (b * b) == c:
                return True
    return False


def better_brute_force(c: int) -> bool:
    MAX_SQUARE: int = int(c ** 0.5) + 1
    for a in range(0, MAX_SQUARE):
        b = c - (a * a)
        i, sum = 1, 0
        while sum < b:
            sum += i
            i += 2
        
        if (sum == b):
            return True
    
    return False


def another_solution(c: int) -> bool:
    MAX_SQUARE: int = int(c ** 0.5) + 1
    for a in range(MAX_SQUARE):
        b: int = c - (a * a)
        target: float = b ** 0.5
        if int(target) == target:
            return True
        
    return False


def binary_search(c: int) -> bool:
    MAX_SQUARE: int = int(c ** 0.5) + 1
    for a in range(MAX_SQUARE):
        target: int = c - (a * a)
        start, end = 0, target
        while start <= end:
            middle: int = start + (end - start) // 2
            compare: int = middle * middle
            
            if compare > target:
                end = middle - 1
            elif compare < target:
                start = middle + 1
            else:
                return True
    
    return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | bool]] = [
        { "input": {"c": 5}, "output": True },
        { "input": {"c": 3}, "output": False },
        { "input": {"c": 2}, "output": True },
        { "input": {"c": 1}, "output": True },
        { "input": {"c": 0}, "output": True },
        { "input": {"c": 10000000}, "output": True }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == brute_force(**case["input"])
        assert case["output"] == better_brute_force(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == binary_search(**case["input"])
        