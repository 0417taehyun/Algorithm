# [ 백준 ] 2839번: 설탕 배달

def solution() -> None:
    N: int = int(input())
    
    answer: int = 0
    while N > 0:
        if N % 5 == 0:
            answer += 1
            N -= 5
        
        else:
            answer += 1
            N -= 3
    
    if N < 0:
        print(-1)
    else:
        print(answer)
        

if __name__ == "__main__":
    import io
    import unittest.mock    
    

    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=["18"]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "4\n"
            
            
    test_example_case()
    