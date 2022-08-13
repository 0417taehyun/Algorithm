# [ 백준 ] 11660번: 구간 합 구하기 5

def solution() -> None:
    import sys


    input = sys.stdin.readline
    N, M = map(int, input().split())
    array: list[int] = [ list(map(int, input().split())) for _ in range(N) ]
    dp: list[int] = [ [0] * (N+1) for _ in range(N+1) ]

    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + array[i][j]
    
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2] - (dp[x2][y1-1] + dp[x1-1][y2]) + dp[x1-1][y1-1])

        
if __name__ == "__main__" :
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str]] | str] = [
        {
            "input": [
                "4 3", "1 2 3 4", "2 3 4 5", "3 4 5 6", "4 5 6 7",
                "2 2 3 4", "3 4 3 4", "1 1 4 4"
            ],
            "output": "27\n6\n64\n"
        },
        {
            "input": [
                "2 4", "1 2", "3 4",
                "1 1 1 1", "1 2 1 2", "2 1 2 1", "2 2 2 2"
            ],
            "output": "1\n2\n3\n4\n"
        },            
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        