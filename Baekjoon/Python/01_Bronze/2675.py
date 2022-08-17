# [ 백준 ] 2675번: 문자열 제출

def solution() -> None:
    import sys


    input = sys.stdin.readline
    for _ in range(int(input())):
        R, S = input().split()
        print("".join([character * int(R) for character in S]))


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ["2", "3 ABC", "5 /HTP"],
        "output": "AAABBBCCC\n/////HHHHHTTTTTPPPPP\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    