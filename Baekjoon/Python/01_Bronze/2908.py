# [ 백준 ] 2908번: 상수

def solution() -> None:
    A, B = map(lambda number: "".join(list(reversed(number))), input().split())
    print(A if int(A) > int(B) else B)
    
    
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
    
        
    cases: list[dict, list[str] | str] = [
        {
            "input": ["734 893"],
            "output": "437\n",
        },
        {
            "input": ["221 231"],
            "output": "132\n",
        },
        {
            "input": ["839 237"],
            "output": "938\n",
        }                
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        