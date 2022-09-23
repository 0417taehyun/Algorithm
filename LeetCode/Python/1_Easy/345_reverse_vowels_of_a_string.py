# [ LeetCode ] 345. Reverse Vowels of a String

def solution(s: str) -> str:
    VOWELS: set = { "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
        
    characters: list[str] = list(s)
    left, right = 0, len(characters) - 1
    while left < right:
        left_value, right_value = characters[left], characters[right]
        if left_value in VOWELS and right_value in VOWELS:
            characters[left], characters[right] = (
                characters[right], characters[left]
            )
            left += 1
            right -= 1
        elif left_value in VOWELS and right_value not in VOWELS:
            right -= 1
        elif left_value not in VOWELS and right_value in VOWELS:
            left += 1
        else:
            left += 1
            right -= 1
    
    return "".join(characters)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": {"s": "hello"},
            "output": "holle"
        },
        {
            "input": {"s": "leetcode"},
            "output": "leotcede"
        },
        {
            "input": {"s": "aA"},
            "output": "Aa"
        }                        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
