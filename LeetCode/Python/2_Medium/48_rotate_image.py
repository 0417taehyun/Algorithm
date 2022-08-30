# [ LeetCode ] 48. Rotate Image

def solution(matrix: list[list[int]]) -> list[list[int]]:
    def recursive_rotate(
        previous: int,
        row: int,
        column: int,
        start_row: int,
        start_column: int,
    ):
        if row != start_row or column != start_column:
            temp = matrix[row][column]
            matrix[row][column] = previous
            return recursive_rotate(
                previous=temp,
                row=column,
                column=N-1-row,
                start_row=start_row,
                start_column=start_column
            )
        
        else:
            matrix[row][column] = previous
        
        
    N: int = len(matrix)
    for row in range(N//2):
        for column in range(row, N-1-row):
            recursive_rotate(
                previous=matrix[row][column],
                row=column,
                column=N-1-row,
                start_row=row,
                start_column=column
            )

    return matrix


def another_solution(matrix: list[list[int]]) -> None:    
    def transpose() -> None:
        for i in range(N):
            for j in range(i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
    def reflect() -> None:
        for i in range(N):
            for j in range(N//2):
                matrix[i][j], matrix[i][N-1-j] \
                    = matrix[i][N-1-j], matrix[i][j]
    
    
    N: int = len(matrix)    
    transpose()
    reflect()
    return matrix


if __name__ == "__main__":
    import copy
    
    cases: list[dict[str, dict[str, list[list[int]]] | list[list[int]]]] = [
        {
            "input": {
                "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            },
            "output": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        },
        {
            "input": {
                "matrix": [
                    [5, 1, 9, 11, 999, 998, 997],
                    [995, 2, 4, 8, 10, 55, 64],
                    [994, 993, 992, 13, 3, 6, 7],
                    [991, 990, 989, 15, 14, 12, 16],
                    [100, 101, 102, 103, 104, 105, 106],
                    [200, 201, 202, 203, 204, 205, 206],
                    [300, 301, 302, 303, 304, 305, 306]
                ]
            },
            "output": [
                [300, 200, 100, 991, 994, 995, 5],
                [301, 201, 101, 990, 993, 2, 1],
                [302, 202, 102, 989, 992, 4, 9],
                [303, 203, 103, 15, 13, 8, 11],
                [304, 204, 104, 14, 3, 10, 999],
                [305, 205, 105, 12, 6, 55, 998],
                [306, 206, 106, 16, 7, 64, 997]
            ]
        },        
    ]
    for case in cases:
        assert case["output"] == solution(
            matrix=copy.deepcopy(case["input"]["matrix"])
        )
        assert case["output"] == another_solution(
            matrix=copy.deepcopy(case["input"]["matrix"])
        )
        
    