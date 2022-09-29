# [ LeetCode ] 744. Find Smallest Letter Greater Than Target

def solution(letters: list[str], target: str) -> str:
    if letters[-1] <= target:
        return letters[0]
    else:
        start, end = 0, len(letters) - 1
        while start <= end:
            middle: int = (start + end) // 2
            if letters[middle] <= target:
                start = middle + 1
            else:
                end = middle - 1
                
        return letters[start]


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[str] | str] | str]] = [
        {
            "input": {
                "letters": ["c", "f", "g"],
                "target": "a"
            },
            "output": "c"
        },
        {
            "input": {
                "letters": ["c", "f", "g"],
                "target": "c"
            },
            "output": "f"
        },
        {
            "input": {
                "letters": ["c", "f", "g"],
                "target": "d"
            },
            "output": "f"
        },
        {
            "input": {
                "letters": ["c", "f", "g"],
                "target": "z"
            },
            "output": "c"
        }                  
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
    