# [ LeetCode ] 2351. First Letter to Appear Twice

def solution(s: str) -> str:
    seen: set = set()
    for character in s:
        if character in seen:
            return character
        else:
            seen.add(character)

if __name__ == "__main__":
    cases: list[dict[str, dict[str, str]] | str] = [
        {
            "input": {"s": "abccbaacz"},
            "output": "c"
        },
        {
            "input": {"s": "abcdd"},
            "output": "d"
        }       
    ]
    for case in cases:
        assert case["output"] == solution(s=case["input"]["s"])
