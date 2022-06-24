# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 모험가 길드

def solution() -> None:    
    from collections import defaultdict
    
    
    N: int = int(input())
    F: list(int) = list(map(int, input().split()))
    
    fearnesses: dict[int, int] = defaultdict(int)
    for fearness in F:
        fearnesses[fearness] += 1
    
    answer: int = 0
    for fearness, count in fearnesses.items():
        answer += (count // fearness)
    
    print(answer)
            

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["5", "2 3 1 2 2"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "2\n"
    
    
    test_example_case()
    