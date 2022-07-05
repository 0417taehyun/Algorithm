# [ 백준 ] 1541번: 잃어버린 괄호

def solution() -> None:
    N: str = input() + '+'
    
    answer: int = 0
    current_num: str = ""
    current_sum: list = []
    current_operation: str = '+'
    for character in N:
        if character == '+':
            current_sum.append(int(current_num))
            current_num = ""
        
        elif character == '-':
            current_sum.append(int(current_num))
            
            if current_operation == '+':
                answer += sum(current_sum)
            
            else:
                answer -= sum(current_sum)
            
            current_num = ""
            current_sum = []
            current_operation = '-'
        
        else:
            current_num += character
    
    if current_operation == '+':
        answer += sum(current_sum)
    
    else:
        answer -= sum(current_sum)
    
    
    print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    
    def test_example_case(case: dict[str, list[str] | int]) -> str:
        with patch("builtins.input", side_effect=case["input"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            output: int = case["output"]
            assert test_stdout.getvalue() == f"{output}\n"

    
    cases: list[dict[str, list[str] | int]] = [
        {"input": ["55-50+40"], "output": -35},
        {"input": ["10+20+30+40"], "output": 100},
        {"input": ["00009-00009"], "output": 0},
    ]
    for case in cases:
        test_example_case(case=case)
