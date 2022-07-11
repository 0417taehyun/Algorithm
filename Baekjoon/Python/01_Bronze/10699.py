# [ 백준 ] 10699번: 오늘 날짜

def solution() -> None:
    from datetime import datetime, timezone, timedelta

    print(
        datetime.strftime(
            datetime.now(tz=timezone(timedelta(hours=9))),
            "%Y-%m-%d"
        )
    )


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]):
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
    
        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": [],
        "output": "2022-07-11"
    }
    
    output: str = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
    