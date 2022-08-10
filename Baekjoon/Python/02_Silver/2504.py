# [ 백준 ] 2504번: 괄호의 값

def solution() -> None:
    S: str = input()
    
    values: dict[str, int] = {"(": 2, "[": 3}
    brackets: dict[str, str] = {")": "(", "]": "["}
    
    temp, answer = 1, 0
    stack: list[str] = []
    previous_bracket: str = ""
    is_validated_brackets: bool = True
    for bracket in S:
        if not bracket in brackets:
            temp *= values[bracket]
            stack.append(bracket)
        
        else:
            if not stack:
                is_validated_brackets = False
                break
            
            else:
                compare_bracket: str = stack.pop()
                target_bracket: str = brackets[bracket]
                if compare_bracket != target_bracket:
                    is_validated_brackets = False
                    break
                
                else:
                    if not previous_bracket in brackets:
                        answer += temp
                        
                    temp //= values[target_bracket]

        previous_bracket = bracket

    if stack or not is_validated_brackets:
        print(0)
        
    else:
        print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | int]] = [
        { "input": ["([])"], "output": "6\n" },
        { "input": ["(()[[]])([])"], "output": "28\n" },
        { "input": ["(()[[]])([])(()[[]])([])"], "output": "56\n" },
        { "input": ["(()[[][]])"], "output": "40\n" },
        { "input": ["[][]((])"], "output": "0\n" },
        { "input": ["([())]"], "output": "0\n" },
        { "input": ["]]"], "output": "0\n" },         
        { "input": ["()([]"], "output": "0\n" },
        { "input": ["(())[[]])([])["], "output": "0\n" },        
    ]
    for case in cases:
        print(test_example_case(input=case["input"]))
        assert case["output"] == test_example_case(input=case["input"])
        