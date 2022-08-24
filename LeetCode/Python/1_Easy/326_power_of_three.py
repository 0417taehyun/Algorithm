# [ LeetCode ] 326. Power of Three

def solution(n: int) -> bool:
    if n <= 0:
        return False
    else:
        while (n % 3 == 0):
            n //= 3
            
        return n == 1


def another_solution(n: int) -> bool:
    from math import log
    
    
    max_n: int = (2 ** 31) - 1
    max_x: int = 3 ** int(log(max_n, 3))
    return True if n > 0 and max_x % n == 0 else False
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | bool]] = [
        {"input": {"n": 27}, "output": True},
        {"input": {"n": 0}, "output": False},
        {"input": {"n": 9}, "output": True},
        {"input": {"n": 1}, "output": True},
        {"input": {"n": -81}, "output": False},
        {"input": {"n": 243}, "output": True},
    ]
    for case in cases:
        assert case["output"] == solution(n=case["input"]["n"])
        assert case["output"] == another_solution(n=case["input"]["n"])
        