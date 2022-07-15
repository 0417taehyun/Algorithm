# [ 백준 ] 2420번: 사파리월드

def solution() -> None:
    print((lambda x: abs(x[0] - x[1]))(list(map(int, input().split()))))
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> int:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | int] = {
        "input": ["-2 5"], "output": 7,
    }
    output: int = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    