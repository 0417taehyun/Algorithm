# [ LeetCode ] 191. Number of 1 Bits

def solution(n: int) -> int:
    return bin(n).count("1")


def another_solution(n: int) -> int:
    answer: int = 0
    while n != 0:
        n &= (n - 1)
        answer += 1
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | int]] = [
        {
            "input": {"n": 11},
            "output": 3
        },
        {
            "input": {"n": 128},
            "output": 1
        },
        {
            "input": {"n": 4294967293},
            "output": 31
        }                
    ]
    for case in cases:
        assert case["output"] == solution(n=case["input"]["n"])
        assert case["output"] == another_solution(n=case["input"]["n"])
    