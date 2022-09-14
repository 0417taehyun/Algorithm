# [ LeetCode ] 231. Power of Two

def solution(n: int) -> bool:
    return True if n > 0 and n & (n - 1) == 0 else False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | bool]] = [
        {"input": {"n": 1}, "output": True},
        {"input": {"n": 16}, "output": True},
        {"input": {"n": 3}, "output": False},
        {"input": {"n": 0}, "output": False},
        {"input": {"n": -16}, "output": False}
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
