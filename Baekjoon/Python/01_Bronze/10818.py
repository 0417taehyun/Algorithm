# [ 백준 ] 10818번: 최소, 최대

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N: int = int(input())
    numbers: list[int] = list(map(int, input().split()))
    print(min(numbers), max(numbers))
    
    
def another_solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N: int = int(input())
    numbers: list[int] = list(map(int, input().split()))
    
    min_number, max_number = numbers[0], numbers[0]
    for idx in range(1, N):
        if numbers[idx] > max_number:
            max_number = numbers[idx]
        elif numbers[idx] < min_number:
            min_number = numbers[idx]
    
    print(min_number, max_number)

        
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    

    def test_another_solution(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                another_solution()
                
        return test_stdout.getvalue()    
    
    
    case: dict[str, list[str] | str] = {
        "input": [ "5", "20 10 35 30 7" ],
        "output": "7 35\n"
    }
    assert case["output"] == test_example_case(input=case["input"])    
    assert case["output"] == test_another_solution(input=case["input"])
    