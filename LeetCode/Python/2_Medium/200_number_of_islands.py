# [ LeetCode ] 200. Number of Islands

def solution(grid: list[list[int]]) -> int:
    def validate_island(grid: list[list[int]], row: int, column: int):
        if (
            (row >= 0 and row <len(grid))
            and
            (column >= 0 and column < len(grid[0]))
        ):
            if grid[row][column] == "1":
                grid[row][column] = "0"
                validate_island(grid=grid, row=row-1, column=column)
                validate_island(grid=grid, row=row+1, column=column)
                validate_island(grid=grid, row=row, column=column-1)
                validate_island(grid=grid, row=row, column=column+1)
            
            else:
                return None
        
        else:
            return None
            
    
    answer: int = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "1":
                answer += 1
                validate_island(grid=grid, row=row, column=column)
    
    return answer


def another_solution(grid: list[list[int]]) -> int:
    M, N = len(grid), len(grid[0])
    visited: list[list[bool]] = [[False] * N for _ in range(M)]
    
    
    def dbs(row: int, column: int) -> None:
        if (
            (row >= 0 and row < M)
            and
            (column >= 0 and column < N)
            and
            grid[row][column] == "1"
            and
            not visited[row][column]
        ):
            visited[row][column] = True
            dbs(row=row-1, column=column)
            dbs(row=row+1, column=column)
            dbs(row=row, column=column-1)
            dbs(row=row, column=column+1)

    answer: int = 0
    for row in range(M):
        for column in range(N):
            if grid[row][column] == "1" and not visited[row][column]:
                answer += 1
                dbs(row=row, column=column)
    
    return answer
            
            
if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]]] | int]] = [
        {
            "input": {
                "grid": [    
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]
                ]
            },
            "output": 1
        },
        {
            "input": {
                "grid": [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"]                    
                ]
            },
            "output": 3
        }        
    ]
    for case in cases:
        assert case["output"] == another_solution(grid=case["input"]["grid"])
        assert case["output"] == solution(grid=case["input"]["grid"])
        