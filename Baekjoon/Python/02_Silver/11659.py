# [ 백준 ] 11659번: 구간 합 구하기 4

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N, M = map(int, input().split())
    numbers: list[int] = list(map(int, input().split()))
    dp: list[int] = [0]
    for idx, number in enumerate(numbers):
        dp.append(dp[idx] + number)
    
    for _ in range(M):
        i, j = map(int, input().split())
        print(dp[j] - dp[i-1])


def another_solution() -> None:
    import sys
    from itertools import accumulate
    
    
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dp: list[int] = list(
        accumulate(list(map(int, input().split())), initial=0)
    )
    for _ in range(M):
        i, j = map(int, input().split())
        print(dp[j] - dp[i-1])


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
        "input": ["5 3", "5 4 3 2 1", "1 3", "2 4", "5 5"],
        "output": "12\n9\n1\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    assert case["output"] == test_another_solution(input=case["input"])
    