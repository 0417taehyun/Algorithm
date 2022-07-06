# [ 백준 ] 1946번: 신입사원

def solution() -> None:
    T: int = int(input())
    for _ in range(T):
        N: int = int(input())
        answer: int = 1
        candidates: list[tuple[int, int]] = []
        for _ in range(N):
            candidates.append(tuple(map(int, input().split())))
        
        candidates = sorted(candidates, key=lambda x: x[0])
        minimum_score: int = candidates[0][1]
        for _, b_test in candidates[1:]:
            if minimum_score > b_test:
                answer += 1
                minimum_score = b_test
        
        print(answer)
        

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(case: dict[str, list[str] | str]) -> None:
        with patch("builtins.input", side_effect=case["input"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        assert case["output"] == test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": [
                '2', '5', "3 2", "1 4", "4 1", "2 3", "5 5",
                '7', "3 6", "7 3", "4 2", "1 4", "5 7", "2 5", "6 1",
            ],
            "output": "4\n3\n"
        },
    ]
    for case in cases:
        test_example_case(case=case)
        