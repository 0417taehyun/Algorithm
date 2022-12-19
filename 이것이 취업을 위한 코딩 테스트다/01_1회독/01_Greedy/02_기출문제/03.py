# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 문자열 뒤집기

def solution() -> None:
    S: str = input()
    
    answer: int = 0
    first_num, previous_num = S[0], S[0]
    for num in S:
        if (num != first_num) and (num != previous_num):
            previous_num = num
            answer += 1
            
        elif num != previous_num:
            previous_num = num
    
    print(answer)
            

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["0001100"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "1\n"
    
    
    test_example_case()
    