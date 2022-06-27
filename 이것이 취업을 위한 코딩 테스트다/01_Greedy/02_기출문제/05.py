# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 볼링공 고르기

def solution() -> None:
    from collections import defaultdict


    N, M = list(map(int, input().split()))
    balls: dict[int, int] = defaultdict(int)
    for ball in list(map(int, input().split())):
        balls[ball] += 1
    
    answer: int = 0
    for ball_count in balls.values():
        answer += ((N - ball_count) * ball_count)
    
    print(answer // 2)
            

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["6 3", "1 3 2 2 3 3"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "11\n"
    
    
    test_example_case()
