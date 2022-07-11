# [ 백준 ] 1008번: A/B

def solution() -> None:
    print((lambda x: x[0]/x[1])(list(map(int, input().split()))))


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
            "input": ["1 3"],
            "output": 0.33333333333333333333333333333333
        },
        {
            "input": ["4 5"],
            "output": 0.8
        },        
    ]
    
    for case in cases:
        output: str = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
        