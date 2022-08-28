# [ LeetCode ] 1137. N-th Tribonacci Number

def solution(n: int) -> int:
    dp: list[int] = [0] * (n + 1)
    for idx in range(1, n + 1):
        if idx <= 2:
            dp[idx] = 1
        else:
            dp[idx] = dp[idx - 3] + dp[idx - 2] + dp[idx - 1]
        
    return dp[n]


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        { "input": {"n": 4}, "output": 4 },
        { "input": {"n": 25}, "output": 1389537 },
    ]
    for case in cases:
        assert case["output"] == solution(n=case["input"]["n"])
    