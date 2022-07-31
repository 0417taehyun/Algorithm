# [ 백준 ] 10815반: 숫자 카드

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N: int = int(input())
    cards: list[int] = sorted(list(map(int, input().split())))
    M: int = int(input())
    
    for target in list(map(int, input().split())):
        flag: int = 0
        start, end = 0, N-1
        while start <= end:
            middle = (start + end) // 2
            card = cards[middle]
            
            if target == card:
                flag = 1
                break
            
            elif target < card:
                end = middle - 1
                
            else:
                start = middle + 1
        
        print(flag, end=" ")
    

def another_solution() -> None:
    import sys
    import bisect
    
    
    input = sys.stdin.readline
    N: int = int(input())
    cards: list[int] = sorted(list(map(int, input().split())))
    M: int = int(input())
    
    for target in list(map(int, input().split())):
        left_value = bisect.bisect_left(a=cards, x=target)
        right_value = bisect.bisect_right(a=cards, x=target)
        
        print(0, end=" ") if not(right_value - left_value) else print(1, end=" ")
        
        
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()

        return test_stdout.getvalue()
    

    def test_another_solution(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                another_solution()

        return test_stdout.getvalue()    
    
    case: dict[str, list[str] | str] = {
        "input": ['5', "6 3 2 10 -10", '8', "10 9 -5 2 3 4 5 -10"],
        "output": "1 0 0 1 1 0 0 1 "
    }
    assert case["output"] == test_example_case(input=case["input"])
    assert case["output"] == test_another_solution(input=case["input"])
    