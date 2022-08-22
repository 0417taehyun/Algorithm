# [ 백준 ] 11720번: 숫자의 합

def solution() -> None:
    N: int = int(input())
    print(sum(map(int, list(input()))))
    

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
            "input": ["1", "1"],
            "output": "1\n"
        },
        {
            "input": ["5", "54321"],
            "output": "15\n"
        },
        {
            "input": ["25", "7000000000000000000000000"],
            "output": "7\n"
        },
        {
            "input": ["11", "10987654321"],
            "output": "46\n"
        }                        
    ]
    
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        