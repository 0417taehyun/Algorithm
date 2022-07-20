# [ 뱍쥰 ] 2741번: N 찍기

def solution() -> None:
    [ print(num) for num in range(1, int(input())+1) ]


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ['5'],
        "output": "1\n2\n3\n4\n5\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    