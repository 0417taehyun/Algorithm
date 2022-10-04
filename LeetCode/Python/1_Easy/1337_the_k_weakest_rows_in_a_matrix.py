# [ LeetCode ] 1337. The K Weakest Rows in a Matrix

def solution(mat: list[list[int]], k: int) -> list[int]:
    rows: dict[int, int] = {}
    for index, row in enumerate(mat):
        start, end = 0, len(row) - 1
        while start <= end:
            middle: int = start + (end - start) // 2
            if row[middle] == 0:
                end = middle - 1
            else:
                start = middle + 1
                
        rows[index] = start
    
    answer: list[int] = []
    for row, _ in sorted(rows.items(), key=lambda x: (x[1], x[0])):
        if k >= 1:
            answer.append(row)
            k -= 1
            
        else:
            break
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]] | int] | list[int]]] = [
        {
            "input": {
                "mat": [
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1],  
                ],
                "k": 3
            },
            "output": [2, 0, 3]
        },
        {
            "input": {
                "mat": [
                    [1, 0, 0, 0],
                    [1, 1, 1, 1],
                    [1, 0, 0, 0],
                    [1, 0, 0, 0],
                ],
                "k": 2
            },
            "output": [0, 2]
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        