# [ LeetCode ] 739. Daily Temperatures

def solution(temperatures: list[int]) -> list[int]:
    answer: list[int] = [0] * len(temperatures)
    stack: list[int] = []
    for current_day, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            previous_day: int = stack.pop()
            difference: int = current_day - previous_day
            answer[previous_day] = difference
        stack.append(current_day)
    return answer


def another_solution(temperatures: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    cases: list[dict[str, list[int] | list[int]]] = [
        {
            "input": {
                "temperatures": []
            },
            "output": []
        },
        {
            "input": {
                "temperatures": []
            },
            "output": []
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        