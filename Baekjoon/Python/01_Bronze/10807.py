# [ 백준 ] 10807번: 개수 세기

def solution() -> None:
    N: int = int(input())
    numbers: list[int] = list(map(int, input().split()))
    v: int = int(input())
    
    answer: int = 0
    for number in numbers:
        if number == v:
            answer += 1
            
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
        {"input": ["11", "1 4 1 2 4 2 4 2 3 4 4", '2'], "output": "3\n"},
        {"input": ["11", "1 4 1 2 4 2 4 2 3 4 4", '5'], "output": "0\n"},
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        