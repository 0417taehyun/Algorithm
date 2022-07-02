# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 뱀

def solution() -> None:
    N: int = int(input())
    map_info: list[int] = [ [0] * N for _ in range(N) ]
    for _ in range(int(input())):
        x, y = list(map(int, input().split()))
        map_info[x-1][y-1] += 1

    move_info: dict[int, str] = {}
    for _ in range(int(input())):
        time, direction = input().split()
        move_info[int(time)] = direction

    visited_info: list = []
    moved_measure: list[tuple(int, int)] = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
    
    current_x: int = 0
    current_y: int = 0
    current_direction: int = 0
    
    answer: int = 0
    while True:
        answer += 1
        x_destination = current_x + moved_measure[current_direction][0]
        y_destination = current_y + moved_measure[current_direction][1]

        if (x_destination > (N-1)) or (y_destination > (N-1)) or \
            (x_destination < 0) or (y_destination < 0):
            break
        
        elif (x_destination, y_destination) in visited_info:
            break

        else:
            visited_info.append((current_x, current_y))
            current_x, current_y = x_destination, y_destination

            if map_info[x_destination][y_destination] == 1:
                map_info[x_destination][y_destination] = 0

            else:
                visited_info.pop(0)

        if answer in move_info.keys():
            if move_info[answer] == 'L':
                current_direction -= 1
                if current_direction == -1:
                    current_direction = 3

            else:
                current_direction += 1
                if current_direction == 4:
                    current_direction = 0

    print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    

    def test_example_case(case: dict[str, list[str] | int]) -> None:
        with patch("builtins.input", side_effect=case["input"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
            
            output: int = case["output"]
            assert test_stdout.getvalue() == f"{output}\n"
    

    cases: list[dict[str, list[str] | int]] = [
        {
            "input": [
                '6', '3', '3 4', "2 5", "5 3", '3', "3 D", "15 L", "17 D",
            ],
            "output": 9,
        },
        {
            "input": [
                "10", '4', "1 2", "1 3", "1 4", "1 5", '4', "8 D", "10 D",
                "11 D", "13 L",
            ],
            "output": 21,
        },
        {
            "input": [
                "10", '5', "1 5", "1 3", "1 2", "1 6", "1 7", '4', "8 D",
                "10 D", "11 D", "13 L",
            ],
            "output": 13,
        }                
    ]
    for case in cases:
        test_example_case(case=case)
