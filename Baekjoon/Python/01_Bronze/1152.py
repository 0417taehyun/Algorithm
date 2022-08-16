# [ 백준 ] 1152번: 단어의 개수

def solution() -> None:
    import re
    import sys
    
    
    input = sys.stdin.readline
    print(len(re.findall(r"[a-zA-Z]+", input())))
    
    
def another_solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    print(len(input().split()))
    
    
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    def test_another_solution(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                another_solution()
    
        return test_stdout.getvalue()    
    
    
    cases: list[dict, list[str] | str] = [
        {
            "input": ["The Curious Case of Benjamin Button"],
            "output": "6\n"
        },
        {
            "input": [" The first character is a blank"],
            "output": "6\n"
        },
        {
            "input": ["The last character is a blank "],
            "output": "6\n"
        }                
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        assert case["output"] == test_another_solution(input=case["input"])
    
    