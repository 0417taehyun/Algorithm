# [ 백준 ] 18111번: 마인크래프트

def calculate_time(
    N: int,
    M: int,
    B: int,
    target_height: int,
    map_info: list[list[int]]
) -> int:
    total_time: int = 0

    for i in range(N):
        for j in range(M):
            if target_height > map_info[i][j]:
                added_block: int = target_height - map_info[i][j]
                total_time += 1
                B -= added_block

            elif target_height < map_info[i][j]:
                removed_block: int = map_info[i][j] - target_height
                total_time += 2
                B += removed_block

        if B < 0:
            return -1

    return total_time


def failed_solution() -> None:
    N, M, B = map(int, input().split())
    map_info: list[int[int]] = [ [0] * M for _ in range(N) ]

    biggest_num: int = -1
    smallest_num: int = 257
    for i in range(N):
        map_input: list[int] = list(map(int, input().split()))
        for j in range(M):
            if map_input[j] > biggest_num:
                biggest_num = map_input[j]
            
            elif map_input[j] < smallest_num:
                smallest_num = map_input[j]
            
            map_info[i][j] = map_input[j]

    answer: list[int, int] = [255 * N * M, -1]
    for height in range(smallest_num, biggest_num + 1):
        spent_time: int = calculate_time(
            N=N, M=M, B=B, target_height=height, map_info=map_info
        )
        if (answer[0] > spent_time) or \
            ((answer[0] == spent_time) and (answer[1] < height)):
            answer = [spent_time, height]

    print(answer[0], answer[1])


def solution() -> None:
    from collections import defaultdict


    N, M, B = map(int, input().split())

    biggest_num: int = -1
    smallest_num: int = 257
    heights: dict[int, int] = defaultdict(int)

    for _ in range(N):
        map_info: list[list[int]] = list(map(int, input().split()))
        for j in range(M):
            if biggest_num < map_info[j]:
                biggest_num = map_info[j]
            
            elif smallest_num > map_info[j]:
                smallest_num = map_info[j]
            
            heights[map_info[j]] += 1

    answer_time: int = 256 * N * M
    answer_height: int = -1
    for target_height in range(smallest_num, biggest_num + 1):
        left_block: int = B
        spent_time: int = 0
        for height, count in heights.items():
            if target_height > height:
                added_block: int = (target_height - height)
                left_block -= (added_block * count)
                spent_time += (1 * count * added_block)
            
            elif target_height < height:
                removed_block: int  = (height - target_height)
                left_block += (removed_block * count)
                spent_time += (2 * count * removed_block)

        if (left_block >= 0) and ((answer_time > spent_time) or \
            ((answer_time == spent_time) and (answer_height < target_height))):
            answer_time = spent_time
            answer_height = target_height

    print(answer_time, answer_height)


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
            "input": [
                "3 4 99",
                "0 0 0 0",
                "0 0 0 0",
                "0 0 0 1",
            ],
            "output": "2 0",
        },
        {
            "input": [
                "3 4 1",
                "64 64 64 64",
                "64 64 64 64",
                "64 64 64 63",
            ],
            "output": "1 64",
        },
        {
            "input": [
                "4 4 36",
                "15 43 61 21",
                "19 33 31 55",
                "48 63 1 30",
                "31 28 3 8",
            ],
            "output": "355 32",
        },
        {
            "input": [
                "3 4 11",
                "29 51 54 44",
                "22 44 32 62",
                "25 38 16 2",
            ],
            "output": "250 35"
        }
    ]
    for case in cases:
        output: str = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
