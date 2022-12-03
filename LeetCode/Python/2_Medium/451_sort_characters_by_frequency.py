# [ LeetCode ] 451. Sort Characters By Frequency

def solution(s: str) -> str:
    from collections import defaultdict
    
    
    answer: str = ""
    letters_count: dict[str, int] = defaultdict(int)
    for letter in s:
        letters_count[letter] += 1
    
    sorted_letters_count: list[tuple[str, int]] = sorted(
        letters_count.items(), key=lambda entry: entry[1], reverse=True
    )
    for letter, count in sorted_letters_count:
        answer += (letter * count)
    
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": {"s": "tree"},
            "output": "eetr"
        },
        {
            "input": {"s": "cccaaa"},
            "output": "cccaaa"
        },
        {
            "input": {"s": "Aabb"},
            "output": "bbAa"
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        