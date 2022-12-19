# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 숫자 카드 게임

def solution() -> None:
    N, M = list(map(int, input().split()))
    
    answer: int = 0
    for _ in range(N):
        smallest_card: int = 10000
        for card in list(map(int, input().split())):
            if card < smallest_card:
                smallest_card = card
                
        if answer < smallest_card:
            answer = smallest_card
    
    print(answer)
            

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["2 4", "7 3 1 8", "3 3 3 4"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "3\n"
    
    
    test_example_case()
    