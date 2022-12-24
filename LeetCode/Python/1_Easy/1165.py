# [ LeetCode ] 1165. Single-Row Keyboard

def solution(keyboard: str, word: str) -> int:
    answer: int = 0
    current_index: int = 0
    keyboard_position: dict[str, int] = {
        letter: index for index, letter in enumerate(keyboard)
    }
    for letter in word:
        position: int = keyboard_position[letter]
        answer += abs(position - current_index)
        current_index = position
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | int]] = [
        {
            "input": {
                "keyboard": "abcdefghijklmnopqrstuvwxyz",
                "word": "cba"
            },
            "output": 4
        },
        {
            "input": {
                "keyboard": "pqrstuvwxyzabcdefghijklmno",
                "word": "leetcode"
            },
            "output": 73
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        