# [ 백준 ] 2920번: 음계

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    scale: list[int] = list(map(int, input().split()))
    previous_scale: int = scale[0]
    asc_cnt, desc_cnt = 0, 0
    for s in scale[1:]:
        if s > previous_scale:
            asc_cnt += 1
        else:
            desc_cnt += 1
        
        previous_scale = s
    
    if asc_cnt == (len(scale) - 1):
        print("ascending")
    elif desc_cnt == (len(scale) - 1):
        print("descending")
    else:
        print("mixed")
    
    
        
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": [ "1 2 3 4 5 6 7 8" ],
            "output": "ascending\n"
        },
        {
            "input": [ "8 7 6 5 4 3 2 1" ],
            "output": "descending\n"
        },
        {
            "input": [ "8 1 7 2 6 3 5 4" ],
            "output": "mixed\n"
        }
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])