# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 1이 될 때까지

def solution() -> None:
    N, K = list(map(int, input().split()))
    
    answer: int = 0
    while N > 1:
        if not N % K:
            answer += 1
            N //= K
            
        else:
            answer += 1
            N -= 1
    
    print(answer)
    

def another_solution() -> None:
    N, K = list(map(int, input().split()))
    
    answer: int = 0
    while N >= K:
        answer += (N % K) + 1
        N //= K

    answer += (N - 1)
    
    print(answer)
        

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["25 3"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "6\n"
    
    
    test_example_case()
    