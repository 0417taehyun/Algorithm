# [ LeetCode ] 1119. Remove Vowels from a String

def solution(s: str) -> str:
    VOWELS: set = { "a", "e", "i", "o", "u" }
    answer: str = ""
    for character in s:
        if character not in VOWELS:
            answer += character
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": {"s": "leetcodeisacommunityforcoders"},
            "output": "ltcdscmmntyfrcdrs"
        },
                {
            "input": {"s": "aeiou"},
            "output": ""
        }
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        