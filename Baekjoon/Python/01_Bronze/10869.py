# [ 백준 ] 10869번: 사칙연산

def solution() -> None:
    A, B = map(int, input().split())
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ["7 3"],
        "output": "10\n4\n21\n2\n1"
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    