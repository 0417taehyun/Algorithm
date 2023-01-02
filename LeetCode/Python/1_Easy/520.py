# [ LeetCode ] 520. Detect Capital

def solution(word: str) -> bool:
    start: int = ord('A')
    end: int = ord('Z')
    capitals: set[str] = { chr(start + idx) for idx in range(end-start+1) }
    capital_count: int = 0
    for character in word:
        if character in capitals:
            capital_count += 1
    if capital_count == len(word) or capital_count == 0:
        return True
    if capital_count == 1 and word[0] in capitals:
        return True
    return False


def another_solution(word: str) -> bool:
    import re


    return re.fullmatch(r"[A-Z]+|.[a-z]*", word)

    