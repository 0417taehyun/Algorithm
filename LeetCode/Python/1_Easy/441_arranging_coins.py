# [ LeetCode ] 441. Arranging Coins

def solution(n: int) -> int:
    stair: int = 1
    while n >= stair:
        n -= stair
        stair += 1
    return stair - 1


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        { "input": { "n": 5 }, "output": 2 },
        { "input": { "n": 8 }, "output": 3 }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        