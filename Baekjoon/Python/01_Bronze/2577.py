# [ 백준 ] 2577번: 숫자의 개수

def solution() -> None:
    import sys


    input = sys.stdin.readline
    multiplied_numbers: str = str(int(input()) * int(input()) * int(input()))
    numbers: dict[int, int] = { number: 0 for number in range(10) }
    for number in multiplied_numbers:
        numbers[int(number)] += 1

    for count in numbers.values():
        print(count)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ["150", "266", "427"],
        "output": "3\n1\n0\n2\n0\n0\n0\n2\n0\n0\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    