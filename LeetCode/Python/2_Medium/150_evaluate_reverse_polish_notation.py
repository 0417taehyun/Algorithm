# [ LeetCode ] 150. Evaluate Reverse Polish Notation

def solution(tokens: list[str]) -> int:
    def get_calculate_result(left: int, right: int, operator: str) -> int:
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        return int(left / right)

    
    OPERATORS: set[str] = {"+", "-", "*", "/"}
    stack: list[int] = []
    for token in tokens:
        if token in OPERATORS:
            right: int = stack.pop()
            left: int = stack.pop()
            result: int = get_calculate_result(left, right, token)
            stack.append(result)
        else:
            number: int = int(token)
            stack.append(number)
    
    answer: int = stack.pop()
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[str]] | int]] = [
        {
            "input": { "tokens": ["2","1","+","3","*"] },
            "output": 9
        },
        {
            "input": { "tokens": ["4","13","5","/","+"] },
            "output": 6
        },
        {
            "input": {
                "tokens": [
                    "10","6","9","3","+","-11","*","/","*","17","+","5","+"
                ]
            },
            "output": 22
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
