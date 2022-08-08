# [ 백준 ] 2750번: 수 정렬하기

def solution() -> None:
    N: int = int(input())
    numbers: list[int] = [ int(input()) for _ in range(N) ]
    for number in sorted(numbers):
        print(number)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ["5", "5", "4", "3", "2", "1"],
        "output": "1\n2\n3\n4\n5\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    