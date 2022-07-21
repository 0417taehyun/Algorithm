# [ 백준 ] 10950번: A+B - 3

def solution() -> None:
    [print(sum(list(map(int, input().split())))) for _ in range(int(input()))]
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ['5', "1 1", "2 3", "3 4", "9 8", "5 2"],
        "output": "2\n5\n7\n17\n7\n"
    }
    assert case["output"] == test_example_case(input=case["input"])
    