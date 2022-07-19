# [ 백준 ] 2738번: 행렬 덧셈

def solution() -> None:
    N, M = map(int, input().split())
    A: list[list[int]] = [ list(map(int, input().split())) for _ in range(N) ]
    B: list[list[int]] = [ list(map(int, input().split())) for _ in range(N) ]
    
    for i in range(N):
        for j in range(M):
            print(A[i][j] + B[i][j], end=' ')
        
        print('')
            

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": [
            "3 3", "1 1 1", "2 2 2", "0 1 0",
            "3 3 3", "4 4 4", "5 5 100"
        ],
        "output": "4 4 4 \n6 6 6 \n5 6 100 \n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    