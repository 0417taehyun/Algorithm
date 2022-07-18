# [ 백준 ] 10871번: X보다 작은 수

def solution() -> None:
    N, X = map(int, input().split())
    (
        lambda numbers: [
            print(number, end=' ') for number in numbers
        ]
    )(
        [
            number for number
            in list(map(int, input().split()))
            if number < X 
        ]
    )
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ["10 5", "1 10 4 9 2 3 8 5 7 6"],
        "output": "1 4 2 3 "
    }
    assert case["output"] == test_example_case(input=case["input"])
    