# [ 백준 ] 2805번: 나무 자르기

def solution() -> None:    
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    answer = 0
    max_heigth = max(trees)
    left, right, target = 0, max_heigth, max_heigth // 2
    while left <= right:
        total = sum([ tree - target for tree in trees if tree > target ])
        
        if total >= M:
            if answer < target:
                answer = target
            left = target + 1
            
        else:
            right = target - 1

        target = (left + right) // 2            
        
    print(answer)
    

def another_solution() -> None:
    N, M = map(int, input().split())
    trees: list[int] = list(map(int, input().split()))
    
    start, end = 0, max(trees) - (M // N)
    while start <= end:
        middle: int = (start + end) // 2
        target: int = sum([tree - middle for tree in trees if tree > middle])
        
        if target >= M:
            start = middle + 1
        
        else:
            end = middle - 1
    
    print(end)
        

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
               
        return test_stdout.getvalue()
    
    
    def test_another_solution(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                another_solution()
               
        return test_stdout.getvalue()        
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": ["4 7", "20 15 10 17"],
            "output": "15\n"
        },
        {
            "input": ["5 20", "4 42 40 26 46"],
            "output": "36\n"
        },
        {
            "input": ["5 19", "4 42 40 26 46"],
            "output": "36\n"
        },
        {
            "input": ["1 1", "1"],
            "output": "0\n"
        },
        {
            "input": ["1 1", "2"],
            "output": "1\n"
        }                                     
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        assert case["output"] == test_another_solution(input=case["input"])
    