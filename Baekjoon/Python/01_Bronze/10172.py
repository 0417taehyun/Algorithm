# [ 백준 ] 10172번: 개

def solution() -> None:
    print("|\\_/|")
    print("|q p|   /}")
    print("( 0 )\"\"\"\\")
    print("|\"^\"`    |")
    print("||_/=\\\\__|")


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
        "output": "|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|"
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    