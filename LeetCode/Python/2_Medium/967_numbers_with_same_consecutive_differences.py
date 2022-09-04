# [ LeetCode ] 967. Numbers With Same Consecutive Differences

def solution(n: int, k: int) -> list[int]:
    def validate_number(number: int, target: str) -> None:
        nonlocal seen
        if len(target) == n:
            seen.add(int(target))
        
        elif len(target) < n:
            if (number - k) >= 0:
                new_number: int = number - k
                new_target: str = target + str(number - k)
                validate_number(number=new_number, target=new_target)
            
            if (number + k) <= 9:
                new_number: int = number + k
                new_target: str = target + str(number + k)
                validate_number(number=new_number, target=new_target)

    seen: set = set()        
    for number in range(1, 10):
        validate_number(number=number, target=str(number))
    
    return sorted(seen)


def another_solution(n: int, k: int) -> list[int]:
    pass


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int]] | list[int]] = [
        {
            "input": {"n": 3, "k": 7},
            "output": [181, 292, 707, 818, 929],
        },
        {
            "input": {"n": 2, "k": 1},
            "output": [
                10, 12, 21, 23, 32, 34, 43, 45,
                54, 56, 65, 67, 76, 78, 87, 89, 98
            ],
        },
        {
            "input": {"n": 2, "k": 0},
            "output": [11, 22, 33, 44, 55, 66, 77, 88, 99],
        }                 
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        
    