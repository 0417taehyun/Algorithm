# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 곱하기 혹은 더하기

def solution() -> None:
    S: str = input()
    
    answer: int = int(S[0])
    for idx in range(1, len(S)):
        if (answer <= 1) or (int(S[idx]) <= 1):
            answer += int(S[idx])
        else:
            answer *= int(S[idx])
    
    print(answer)
            

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["02984"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "576\n"
    
    
    test_example_case()
    