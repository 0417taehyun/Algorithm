# [ 백준 ] 11382번: 꼬마 정민

def solution() -> None:
    print(sum(list(map(int, input().split()))))


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    
    case: dict[str, list[str] | int] = {
        "input": ["77 77 7777"],
        "output": 7931
    }

    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
