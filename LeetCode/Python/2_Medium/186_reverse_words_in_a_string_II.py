# [ LeetCode ] 186. Reverse Words in a String II

def solution(s: list[str]) -> list[str]:
    def reverse_word(left: int, right: int, word: list[str]) -> None:
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
    

    left: int = 0
    reverse_word(left, len(s)-1, s)
    for idx, letter in enumerate(s):
        if idx == len(s) - 1:
            reverse_word(left, idx, s)
        elif letter == " ":
            reverse_word(left, idx-1, s)
            left = idx + 1
    
    return s


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[str]] | list[str]]] = [
        {
            "input": {
                "s": [
                    "t", "h", "e", " ",
                    "s", "k", "y", " ",
                    "i", "s", " ",
                    "b", "l", "u", "e"
                ]
            },
            "output": [
                "b", "l", "u", "e", " ",
                "i", "s", " ",
                "s", "k", "y", " ",
                "t", "h", "e"
            ]
        },
        {
            "input": { "s": ["a"] },
            "output": ["a"]
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
