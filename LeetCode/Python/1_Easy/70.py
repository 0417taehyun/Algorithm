# [ LeetCode ] 70. Climbing Stairs

def solution(n: int) -> int:
    answer: int = 0
    before_previous_ways: int = 1
    previous_ways: int = 2
    if n == 1:
        return before_previous_ways
    if n == 2:
        return previous_ways
    for _ in range(3, n+1):
        answer = before_previous_ways + previous_ways
        before_previous_ways = previous_ways
        previous_ways = answer
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        { "input": { "n": 1 }, "output": 1 },
        { "input": { "n": 2 }, "output": 2 },
        { "input": { "n": 3 }, "output": 3 }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
