# [ 백준 ] 10872번: 팩토리얼

def solution() -> None:
    answer: int = 1
    for number in range(1, int(input())+1):
        answer *= number

    print(answer)
        

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    solution()
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": ["10"],
            "output": "3628800\n"
        },
        {
            "input": ['0'],
            "output": "1\n"       
        }
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
    