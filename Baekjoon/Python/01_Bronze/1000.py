# [ 백준 ] 1000번: A+B

def solution() -> None:
    print(sum(map(int, input().split())))

if __name__ == "__main":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | int] = {
        "input": ["1 2"],
        "output": 3
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    