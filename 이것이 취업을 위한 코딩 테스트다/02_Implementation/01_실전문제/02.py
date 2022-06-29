# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 게임 개발

def solution() -> None:
    N, M = list(map(int, input().split()))
    x, y, direction = list(map(int, input().split()))
    map_info: list[list[int]] = [ list(map(int, input().split())) for _ in range(N) ]
    visited_info: list[list[int]] = [ [0] * M for _ in range(N) ]
    
    answer: int = 1
    visited_info[x][y] = 1
    
    circle: int = 0
    move_measures: list[tuple(int, int)] = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
    
    while True:
        if circle == 4:
            x_destination = x - move_measures[direction][0]
            y_destination = y - move_measures[direction][1]
            
            if map_info[x_destination][y_destination] == 1:
                break
                
            else:
                circle = 0
                x, y = x_destination, y_destination
            
        else:
            direction -= 1
            if direction == -1:
                direction = 3
            
            x_destination = x + move_measures[direction][0]
            y_destination = y + move_measures[direction][1]

            if visited_info[x_destination][y_destination] == 0 and \
                map_info[x_destination][y_destination] == 0:
                    circle = 0
                    visited_info[x_destination][y_destination] = 1
                    
                    answer += 1
                    x, y = x_destination, y_destination
            
            else:
                circle += 1
    
    print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
        
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=[
            "4 4",
            "1 1 0",
            "1 1 1 1",
            "1 0 0 1",
            "1 1 0 1",
            "1 1 1 1",
        ]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "3\n"
    
    
    test_example_case()
    