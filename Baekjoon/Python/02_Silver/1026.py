# [ 백준 ] 1026번: 보물

def solution() -> None:
    N: int = int(input())
    A: list[int] = list(map(int, input().split(" ")))
    B: list[int] = list(map(int, input().split(" ")))
    
    answer: int = 0
    for A_num, B_num in zip(sorted(A), sorted(B, reverse=True)):
        answer += (A_num * B_num)
    
    print(answer)
    

def short_solution() -> None:
    N: int = int(input())
    A: list[int] = list(map(int, input().split(" ")))
    B: list[int] = list(map(int, input().split(" ")))
    
    print(sum([ A_num * B_num for A_num, B_num in zip(sorted(A), sorted(B, reverse=True)) ]))
        

if __name__ == "__main__":
    import io
    import unittest.mock
    

    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=["5", "1 1 1 6 0", "2 7 8 3 1"]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "18\n"                
            
 
    test_example_case()
    