# [ 백준 ] 1001번: A-B

def solution() -> None:
    print((lambda x: x[0]-x[1])(list(map(int, input().split()))))


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | int] = {
        "input": ["3 2"],
        "output": 1
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    