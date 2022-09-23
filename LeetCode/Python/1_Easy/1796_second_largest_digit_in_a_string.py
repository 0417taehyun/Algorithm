# [ LeetCode ] 1796. Second Largest Digit in a String

def solution(s: str) -> int:
    maximum_number, answer = -1, -1
    for character in s:
        if character.isdigit():
            number: int = int(character)
            if number > maximum_number:
                maximum_number, answer = number, maximum_number
            elif number < maximum_number and number > answer:
                answer = number
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | int]] = [
        {
            "input": {"s": "dfa12321afd"},
            "output": 2
        },
        {
            "input": {"s": "abc1111"},
            "output": -1
        }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        