# [ LeetCode ] 119. Pascal's Triangle II

def solution(rowIndex: int) -> list[int]:
    answer: list[int] = [1]
    for row in range(1, rowIndex + 1):
        stored: int = answer[0]
        for index in range(1, row):
            stored, answer[index] = answer[index], stored + answer[index]
        
        answer.append(1)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | list[int]]] = [
        {
            "input": { "rowIndex": 3 },
            "output": [1, 3, 3, 1]
        },
        {
            "input": { "rowIndex": 0 },
            "output": [1]
        },
        {
            "input": { "rowIndex": 1 },
            "output": [1, 1]
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        