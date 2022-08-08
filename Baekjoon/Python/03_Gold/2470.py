# [ 백준 ] 2470번: 두 용액

def solution() -> None:
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    answer_l, answer_r = 0, 0
    left, right, diff = 0, N-1, 1000000000*2
    while left < right:
        target = nums[left] + nums[right]
        if abs(target) < diff:
            diff = abs(target)
            answer_l, answer_r = nums[left], nums[right]
            if target == 0:
                break
            
        elif target > 0:
            right -= 1
        
        else:
            left += 1

    print(answer_l, answer_r)    
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": ["5", "-2 4 -99 -1 98"],
            "output": "-99 98\n"
        },
        {
            "input": ["6", "-2 4 1 -99 -1 98"],
            "output": "-1 1\n"            
        },
        {
            "input": ["4", "2 1 -1 0"],
            "output": "-1 1\n"            
        },
        {
            "input": ["4", "2 3 1 4"],
            "output": "1 2\n"            
        },            
        {
            "input": ["4", "-2 -3 -1 -4"],
            "output": "-2 -1\n"            
        },
        {
            "input": ["5", "-2 -3 -1 -4 0"],
            "output": "-1 0\n"            
        }                                     
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
