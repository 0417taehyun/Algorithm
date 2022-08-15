# [ LeetCode ] 13. Roman to Integer

def solution(s: str) -> int:
    answer: int = 0
    rome_to_integer: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    is_minus: bool = False
    previous_symbol: str = ""
    for symbol in s[::-1]:
        if symbol == "I":
            if previous_symbol == "V" or previous_symbol == "X":
                is_minus = True
        
        elif symbol == "X":
            if previous_symbol == "L" or previous_symbol == "C":
                is_minus = True
        
        elif symbol == "C":
            if previous_symbol == "D" or previous_symbol == "M":
                is_minus = True
            
        if is_minus:
            answer -= rome_to_integer[symbol]
        else:
            answer += rome_to_integer[symbol]
            
        is_minus = False
        previous_symbol = symbol
        
    
    return answer


def another_solution(s: str) -> int:
    rome_to_integer: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    reversed_s: str = s[::-1]
    answer: int = rome_to_integer[reversed_s[0]]
    for idx in range(1, len(reversed_s)):
        current_value: int = rome_to_integer[reversed_s[idx]]
        previous_value: int = rome_to_integer[reversed_s[idx-1]]
        
        if current_value < previous_value:
            answer -= current_value
        else:
            answer += current_value
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str]] | int] = [
        {
            "input": {"s": "III"},
            "output": 3
        },
        {
            "input": {"s": "LVIII"},
            "output": 58
        },
        {
            "input": {"s": "MCMXCIV"},
            "output": 1994
        }                
    ]
    for case in cases:
        assert case["output"] == solution(s=case["input"]["s"])
        assert case["output"] == another_solution(s=case["input"]["s"])
        