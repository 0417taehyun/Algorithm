# [ LeetCode ] 69. Sqrt(x)

def solution(x: int) -> int:
    if x <= 1:
        return x
    else:
        answer, start, end = 0, 1, x // 2
        while start <= end:
            middle: int = (start + end) // 2
            if middle * middle > x:
                end = middle = 1
            else:
                answer = middle
                start = middle + 1
        
        return answer


def another_solution(x: int) -> int:
    if x < 2:
        return x
    else:
        start, end = 2, x // 2
        while start <= end:
            middle: int = start + ((end - start) // 2)
            target: int = middle * middle
            
            if target > x:
                end = middle - 1
            elif target < x:
                start = middle + 1
            else:
                return middle
        
        return end


def bit_manipulation(x: int) -> int:
    if x < 2:
        return x
    else:
        left: int = bit_manipulation(x = x >> 2) << 1
        right: int = left + 1
        return left if right * right > x else right
    

def newton_method(x: int) -> int:
    if x <= 1:
        return x
    else:
        previous_x: int = x
        next_x: int = (previous_x + (x / previous_x)) / 2
        
        while previous_x - next_x >= 1:
            previous_x = next_x
            next_x = (previous_x + (x / previous_x)) / 2
        
        return int(next_x)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        { "input": { "x": 0 }, "output": 0 },
        { "input": { "x": 1 }, "output": 1 },
        { "input": { "x": 4 }, "output": 2 },
        { "input": { "x": 8 }, "output": 2 },
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == bit_manipulation(**case["input"])
        assert case["output"] == newton_method(**case["input"])        
    