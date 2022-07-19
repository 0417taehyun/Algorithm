# [ 백준 ] 5597번: 과제 안 내신 분..?

def solution() -> None:
    students: list[int] = [ 0 for _ in range(31) ]
    for _ in range(28):
        students[int(input())] += 1
    
    for idx, student in enumerate(students):
        if idx and not student:
            print(idx)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[int]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | str]] = [
        {
            "input": [
                '3', '1', '4', '5', '7', '9', '6', "10", "11", "12", "13",
                "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                "24", "25", "26", "27", "28", "29", "30"
            ],
            "output": "2\n8\n"
        },
        {
            "input": [
                '9', "30", '6', "12", "10", "20", "21", "11", "7", "5", "28",
                '4', "18", "29", "17", "19", "27", "13", "16", "26", "14",
                "23", "22", "15", '3', '1', "24", "25",
            ],
            "output": "2\n8\n"
        },
    ]
    
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
        