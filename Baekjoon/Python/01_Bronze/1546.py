# [ 백준 ] 1546번: 평균

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N: int = int(input())
    scores: list[int] = list(map(int, input().split()))
    highest_score: int = max(scores)
    new_average_score: float = sum(
        [(score / highest_score) * 100 for score in scores]
    ) / N
    print(new_average_score)


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
            "input": ["3", "40 80 60"],
            "output": "75.0\n",
        },
        {
            "input": ["4", "1 100 100 100"],
            "output": "75.25\n",
        },
        {
            "input": ["5", "1 2 4 8 16"],
            "output": "38.75\n",
        },
        {
            "input": ["2", "3 10"],
            "output": "65.0\n",
        },
        {
            "input": ["4", "10 20 0 100"],
            "output": "32.5\n",
        },
        {
            "input": ["1", "50"],
            "output": "100.0\n",
        }                                                   
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
    