# [ 백준 ] 1874번: 스택 수열

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N: int = int(input())
    result: list[int] = [ int(input()) for _ in range(N) ]
    stack: list[int] = []
    compare_number: int = 1
    answer: str = ""
    is_validate: bool = True
    
    for number in result:
        while number >= compare_number:
            stack.append(compare_number)
            answer += "+\n"
            compare_number += 1
        
        top: int = stack.pop()
        if top == number:
            answer += "-\n"
        else:
            is_validate = False
            break
    
    if is_validate:
        print(answer)
    else:
        print("NO")
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str]] | str] = [
        {
            "input": ["8", "4", "3", "6", "8", "7", "5", "2", "1"],
            "output": "+\n+\n+\n+\n-\n-\n+\n+\n-\n+\n+\n-\n-\n-\n-\n-\n\n"
        },
        {
            "input": ["5", "1", "2", "5", "3", "4"],
            "output": "NO\n"
        }
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        