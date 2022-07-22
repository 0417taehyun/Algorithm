# [ 백준 ] 10952번: A+B - 5

def solution() -> None:
    while answer := sum(list(map(int, input().split()))):
        print(answer)

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()

    
    case: dict[str, list[str] | str] = {
        "input": ["1 1", "2 3", "3 4", "9 8", "5 2", "0 0"],
        "output": "2\n5\n7\n17\n7\n",
    }
    assert case["output"] == test_example_case(input=case["input"])
    