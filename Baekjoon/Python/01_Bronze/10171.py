# [ 백준 ] 10171번: 고양이

def solution() -> None:
    print("\\    /\\")
    print(" )  ( \')")
    print("(  /  )")
    print(" \(__)|")


if __name__ == "__main":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": [],
        "output": "\\    /\\\n )  ( \')\n(  /  )\n \(__)|"
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    