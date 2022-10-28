# [ 백준 ] 1918번: 후위 표기식

def solution() -> None:
    equation: str = input()
    
    answer: str = ""
    stack: list[str] = []
    operators: dict[str, int] = { "(": 0, "+": 1, "-": 1, "*": 2, "/": 2 }
    for expression in equation:
        if expression == "(":
            stack.append(expression)
            
        elif expression == ")":
            while stack:
                operator: str = stack.pop()
                if operator == "(":
                    break
                else:
                    answer += operator
                    
        elif expression in operators:
            while stack:
                operator: str = stack.pop()
                if operators[operator] >= operators[expression]:
                    answer += operator
                else:
                    stack.append(operator)
                    break
            
            stack.append(expression)
        
        else:
            answer += expression
    
    while stack:
        answer += stack.pop()
    
    print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()

        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": ["A*(B+C)"],
            "output": "ABC+*\n"
        },
        {
            "input": ["A+B"],
            "output": "AB+\n"
        },
        {
            "input": ["A+B*C"],
            "output": "ABC*+\n"
        },
        {
            "input": ["A+B*C-D/E"],
            "output": "ABC*+DE/-\n"
        },
        {
            "input": ["(A+((B+C*D)+E))"],
            "output": "ABCD*+E++\n"
        },                      
    ]
    
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        