# [ 백준 ] 9498번: 시험 성적

def solution() -> None:
    score: int = int(input())

    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')    
    elif score >= 60:
        print('D')       
    else:
        print('F')         
        

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {"input": ["100"], "output": 'A'},
        {"input": ["81"], "output": 'B'},
        {"input": ["59"], "output": 'F'},
    ]
    for case in cases:
        output: int = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
        