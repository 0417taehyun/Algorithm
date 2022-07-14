# [ 백준 ] 14681번: 사분면 고르기

def solution() -> None:
    x: int = int(input())
    y: int = int(input())
        
    if (x > 0) and (y > 0):
        print(1)
    elif (x > 0) and (y < 0):
        print(4)
    elif (x < 0) and (y > 0):
        print(2)
    else:
        print(3)
        
        
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> int:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | int]] = [
        {"input": ["12", '5'], "output": 1},
        {"input": ['9', "-13"], "output": 4},
    ]
    for case in cases:
        output: int = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
    