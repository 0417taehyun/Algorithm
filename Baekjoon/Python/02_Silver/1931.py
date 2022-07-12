# [ 백준 ] 1931번: 회의실 배정

def solution() -> None:
    N: int = int(input())
    meetings: list[list[int, int]] = []

    for _ in range(N):
        meetings.append(list(map(int, input().split())))
    
    meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    answer: int = 1
    previous_end_time: int = meetings[0][1]
    for start_time, end_time in meetings[1:]:
        if start_time >= previous_end_time:
            answer += 1
            previous_end_time = end_time

    print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch


    def test_example_case(input: list[str]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()


    case: dict[str, list[str] | int] = {
        "input": [
            '11', "1 4", "3 5", "0 6", "5 7", "3 8",
            "5 9", "6 10", "8 11", "8 12", "2 13", "12 14"
        ],
        "output": 4,
    }
    output: int = case["output"]
    assert f"{output}\n" == test_example_case(input=case["input"])
