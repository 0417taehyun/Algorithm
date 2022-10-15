# [ LeetCode ] 119. Pascal's Triangle II

def solution(rowIndex: int) -> list[int]:
    answer: list[int] = [1]
    for row in range(1, rowIndex + 1):
        stored: int = answer[0]
        for index in range(1, row):
            stored, answer[index] = answer[index], stored + answer[index]
        
        answer.append(1)
    
    return answer


def another_solution(rowIndex: int) -> list[int]:
    answer: list[int] = [1]
    for row in range(1, rowIndex + 1):
        for index in range(row - 1, 0, -1):
            answer[index] = answer[index] + answer[index - 1]
        
        answer.append(1)
    
    return answer
    

def math_solution(rowIndex: int) -> list[int]:
    def combinator(n: int, r: int) -> int:
        top, bottom = 1, 1
        for number in range(n, n - r, -1):
            top *= number
            
        for number in range(r, 0, -1):
            bottom *= number
        
        return top // bottom

    answer: list[int] = [
        combinator(n=rowIndex, r=index)
        for index in range(rowIndex)
    ]
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
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == math_solution(**case["input"])
        