# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 왕실의 나이트

def solution() -> None:
    point: str = input()
    
    answer: int = 0
    moves = ['U', 'R', 'D', 'L']
    for move in moves:
        if move == 'U':
            if int(point[1]) > 2:
                if (point[0] != 'a') and (point[0] != 'h'):
                    answer += 2
                else:
                    answer += 1
            
        elif move == 'R':
            if point[0] < 'g':
                if (int(point[1]) != 1) and (int(point[1]) != 8):
                    answer += 2
                else:
                    answer += 1
        
        elif move == 'D':
            if int(point[1]) < 7:
                if (point[0] != 'a') and (point[0] != 'h'):
                    answer += 2
                else:
                    answer += 1
                    
        elif move == 'L':
            if point[0] > 'b':
                if (int(point[1]) != 1) and (int(point[1]) != 8):
                    answer += 2
                else:
                    answer += 1                    

    print(answer)


def another_solution() -> None:
    point: str = input()
    
    column: int = int(ord(point[0])) - int(ord('a')) + 1
    row: int = int(point[1])
    steps: list[set(int, int)] = [
        (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    
    answer: int = 0
    for row_step, column_step in steps:
        next_row: int = row + row_step
        next_column: int = column + column_step
        
        if (
            (next_row >= 1) and \
                (next_row <= 8) and \
                    (next_column >= 1) and \
                        (next_column <= 8)
        ):
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch


    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["c2"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "6\n"
    
    
    test_example_case()
        