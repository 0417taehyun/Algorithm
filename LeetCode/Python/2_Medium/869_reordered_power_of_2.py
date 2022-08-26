# [ LeetCode ] 869. Reordered Power of 2

def solution(n: int) -> bool:
    from math import log
    
    
    length: int = len(str(n))
    start: int = int(log(10 ** (length - 1), 2))
    end: int = int(log(10 ** length, 2))
    
    for number in range(start, end + 1):
        if sorted(str(n)) == sorted(str(2 ** number)):
            return True
    
    return False


def another_solution(n: int) -> bool:
    numbers: dict[str, int] = {}
    for number in str(n):
        if number in numbers:
            numbers[number] += 1
            
        else:
            numbers[number] = 1
    
    
    for power in range(30):
        target: int = 1 << power
        target_numbers: dict[str, int] = {}
        for number in str(target):
            if number in target_numbers:
                target_numbers[number] += 1
            
            else:
                target_numbers[number] = 1
        
        if numbers == target_numbers:
            return True
    
    
    return False
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        {
            "input": {"n": 1},
            "output": True
        },
        {
            "input": {"n": 10},
            "output": False
        },
        {
            "input": {"n": 4102},
            "output": True
        }        
    ]
    for case in cases:
        assert case["output"] == solution(n=case["input"]["n"])
        assert case["output"] == another_solution(n=case["input"]["n"])
    