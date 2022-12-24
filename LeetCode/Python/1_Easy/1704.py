# [ LeetCode ] 1704. Determine if String Halves Are Alike

def solution(s: str) -> bool:
    VOWELS: set[str] = { "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
    left_count, right_count = 0, 0;
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] in VOWELS:
            left_count += 1
        if s[right] in VOWELS:
            right_count += 1
        
        left += 1
        right -= 1
    
    return left_count == right_count
    
    
if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | bool]] = [
        { "input": { "s": "book" }, "output": True },
        { "input": { "s": "textbook" }, "output": False },
        { "input": { "s": "Uo" }, "output": True }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        