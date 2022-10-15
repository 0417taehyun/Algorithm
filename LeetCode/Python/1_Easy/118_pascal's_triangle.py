# [ LeetCode ] 118. Pascal's Triangle

def solution(numRows: int) -> list[list[int]]:
    answer: list[list[int]] = [[1]]
    for row in range(1, numRows):
        temp: list[int] = [0] * (row + 1)
        for index in range(row + 1):
            if index == 0 or index == row:
                temp[index] = 1
            else:
                temp[index] = (
                    answer[row - 1][index - 1]
                    +
                    answer[row - 1][index]
                )
        
        answer.append(temp)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | list[list[int]]]] = [
        {
            "input": { "numRows": 5 },
            "output": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        },
        {
            "input": { "numRows": 1 },
            "output": [[1]]
        },        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        