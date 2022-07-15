# [ 백준 ] 15552번: 빠른 A+B

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    T: int = int(input())
    for _ in range(T):
        print((lambda x: x[0] + x[1])(list(map(int, input().split()))))


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ['5', "1 1", "12 34", "5 500", "40 60", "1000 1000"],
        "output": "2\n46\n505\n100\n2000\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    