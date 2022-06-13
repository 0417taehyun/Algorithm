# [ 백준 ] 11399번: ATM

def solution() -> None:
    S: str = input()
    
    answer: int = 0
    first_num, current_num = S[0], S[0]
    for num in S:
        if (first_num != num) and (current_num != num):
            current_num = num
            answer +=1
        
        elif current_num != num:
            current_num += num
    
    print(answer)
    

if __name__ == "__main__":
    import io
    import unittest.mock
    

    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=["0001100"]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "1\n"
            
            
    test_example_case()
    