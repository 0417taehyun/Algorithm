# [ 백준 ] 10998번: AxB

def solution() -> None:
    print((lambda x: x[0]*x[1])(list(map(int, input().split()))))


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | int]] = [
        {
            "input": ["1 2"],
            "output": 2
        },
        {
            "input": ["3 4"],
            "output": 12
        },        
    ]
    
    for case in cases:
        output: str = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
    