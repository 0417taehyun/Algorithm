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


def another_solution(mat: list[list[int]], k: int) -> list[int]:
    import heapq
    
    
    n: int = len(mat[0])
    queue: list[tuple[int, int]] = []
    for index in range(len(mat)):
        start, end = 0, n - 1
        while start <= end:
            middle: int = start + (end - start) // 2
            if mat[index][middle] == 0:
                end = middle - 1
            else:
                start = middle + 1
        
        entry: tuple[int, int] = (-start, -index)
        if len(queue) < k or queue[0] < entry:
            heapq.heappush(queue, entry)

        if len(queue) > k:
            heapq.heappop(queue)
        
    answer: list[int] = []
    while queue:
        _, index = heapq.heappop(queue)
        answer.append(-index)
    
    answer.reverse()
    return answer


def vertical_interation(mat: list[list[int]], k: int) -> list[int]:
    answer: list[int] = []
    m, n = len(mat), len(mat[0])
    for column in len(n):
        for row in range(m):
            if (
                len(answer) < k
                and
                mat[row][column] == 0
                and (
                    column == 0
                    or
                    mat[row][column - 1] == 1
                )
            ):
                answer.append(row)

    row: int = 0
    while len(answer) < k:
        if mat[row][-1] == 1:
            answer.append(row)
        row += 1
    
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
        assert case["output"] == another_solution(**case["input"])
        # assert case["output"] == vertical_interation(**case["input"])
        