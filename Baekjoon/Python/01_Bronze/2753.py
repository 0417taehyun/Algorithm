# [ 백준 ] 2753번: 윤년

def solution() -> None:
    year: int = int(input())

    if (not (year % 4) and (year % 100)) or not (year % 400):
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> int:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    

    cases: list[dict[str, list[str] | int]] = [
        {"input": ["2000"], "output": 1},
        {"input": ["1999"], "output": 0},
    ]
    for case in cases:
        output: int = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
        