# [ LeetCode ] 344. Reverse String

def solution(s: str) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        temp: str = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[str]] ]] = [
        {
            "input": { "s": ["h", "e", "l", "l", "o"] },
            "output": ["o", "l", "l", "e", "h"]
        },
        {
            "input": { "s": ["H", "a", "n", "n", "a", "h"] },
            "output": ["h", "a", "n", "n", "a", "H"]
        }        
    ]
    for case in cases:
        solution(**case["input"])
        assert case["output"] == case["input"]["s"]
    