# [ 백준 ] 3052번: 나머지

def solution() -> None:
    seen = { int(input()) % 42 for _ in range(10) }
    print(len(seen))


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
            "input": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            "output": "10\n"
        },
        {
            "input": [
                "42", "84", "252", "420", "840",
                "126", "42", "84", "420", "126"
            ],
            "output": "1\n"
        },
        {
            "input": [
                "39", "40", "41", "42", "43",
                "44", "82", "83", "84", "85"
            ],
            "output": "6\n"
        }                
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])    
    