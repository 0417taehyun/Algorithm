# [ 백준 ] 8958번: OX 퀴즈

def solution() -> None:
    import sys


    input = sys.stdin.readline
    for _ in range(int(input())):
        answer, consecutive_count = 0, 0
        for result in input():
            if result == "O":
                consecutive_count += 1
                answer += consecutive_count
            else:
                consecutive_count = 0
                
        print(answer)
        
        
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": [
            "5", "OOXXOXXOOO", "OOXXOOXXOO", "OXOXOXOXOXOXOX",
            "OOOOOOOOOO", "OOOOXOOOOXOOOOX"
        ],
        "output": "10\n9\n7\n55\n30\n"
    }
    assert case["output"] == test_example_case(input=case["input"])    
            