# [ 백준 ] 2557번: Hello World

def solution() -> None:
    print("Hello World!")


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": [],
        "output": "Hello World!"
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    