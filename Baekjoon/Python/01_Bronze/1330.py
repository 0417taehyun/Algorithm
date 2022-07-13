# [ 백준 ] 1330번: 두 수 비교하기

def solution() -> None:
    A, B = map(int, input().split())

    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print("==")


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {"input": ["1 2"], "output": '<'},
        {"input": ["10 2"], "output": '>'},
        {"input": ["5 5"], "output": "=="},
    ]
    for case in cases:
        output: int = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
        