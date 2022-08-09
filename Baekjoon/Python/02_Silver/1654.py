# [ 백준 ] 1654번: 랜선 자르기

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    K, N = map(int, input().split())
    lans: list[int] = [ int(input()) for _ in range(K) ]
    
    answer: int = 0
    start, end = 1, (max(lans) // (N // K)) + 1
    while start <= end:
        middle: int = (start + end) // 2
        target: int = sum([lan // middle for lan in lans])
        
        if target >= N:
            if answer < middle:
                answer = middle
            start = middle + 1
        else:
            end = middle - 1

    print(answer)    
        

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
            "input": ["4 11", "802", "743", "457", "539"],
            "output": "200\n"
        },
        {
            "input": ["4 4", "400", "400", "400", "400"],
            "output": "400\n"
        }
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
    