# [ 백준 ] 25083번: 새싹

def solution() -> None:
    print("         ,r\'\"7")
    print("r`-_   ,\'  ,/")
    print(" \\. \". L_r\'")
    print("   `~\\/")
    print("      |")
    print("      |")

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
        "output": "         ,r\'\"7\nr`-_   ,\'  ,/\n \\. \". L_r\'\n   `~\\/\n      |\n      |"
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    