# [ LeetCode ] 709. To Lower Case

def solution(s: str) -> str:
    return s.lower()


def another_solution(s: str) -> str:
    difference: int = ord("a") - ord("A")
    return "".join([
        chr(difference + ord(character))
        if ord(character) >= ord("A") and ord(character) <= ord("Z")
        else character
        for character in s
    ])


if __name__ == "__main__":
    cases: list[dict[str, dict[str] | str]] = [
        {
            "input": {"s": "Hello"},
            "output": "hello"
        },
        {
            "input": {"s": "here"},
            "output": "here"
        },
        {
            "input": {"s": "LOVELY"},
            "output": "lovely"
        }           
    ]
    for case in cases:
        assert case["output"] == solution(s=case["input"]["s"])
        assert case["output"] == another_solution(s=case["input"]["s"])
    