# [ LeetCode ] 771. Jewels and Stones

def solution(jewels: str, stones: str) -> int:
    answer: int = 0
    distinct_jewels: set[str] = set(jewels)
    for stone in stones:
        if stone in distinct_jewels:
            answer += 1
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | int]] = [
        {
            "input": {
                "jewels": "aA",
                "stones": "aAAbbbb"
            },
            "output": 3
        },
        {
            "input": {
                "jewels": "z",
                "stones": "ZZ"
            },
            "output": 0
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        