# [ LeetCode ] 342. Power of Four

def solution(n: int) -> bool:
    from math import log
    
    
    return True if n > 0 and int(log(n, 4)) == log(n, 4) else False


def another_solution(n: int) -> bool:
    from math import log
    
    
    max_x: int = (2 ** 31) - 1
    max_n: int = 4 ** int(log(max_x, 4))
    return True if n > 0 and max_n % n == 0 and n % 3 == 1 else False


def recursive_solution(n: int) -> bool:
    if n <= 0:
        return False
    
    else:
        while (n % 4 == 0):
            n //= 4
        
        return n == 1


def bit_manipulation(n: int) -> bool:
    return True if n > 0 and n & (n - 1) == 0 and n % 3 == 1 else False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | bool]] = [
        { "input": { "n": 2 }, "output": False },
        { "input": { "n": 16 }, "output": True },
        { "input": { "n": 5 }, "output": False },
        { "input": { "n": 1 }, "output": True },
        { "input": { "n": 8 }, "output": False },
        { "input": { "n": -64 }, "output": False },
        { "input": { "n": 0 }, "output": False }
    ]
    for case in cases:
        assert case["output"] == solution(n=case["input"]["n"])
        assert case["output"] == another_solution(n=case["input"]["n"])
        assert case["output"] == recursive_solution(n=case["input"]["n"])
        assert case["output"] == bit_manipulation(n=case["input"]["n"])
        