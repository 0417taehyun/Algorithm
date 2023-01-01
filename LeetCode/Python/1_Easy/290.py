# [ LeetCode ] 290. Word Pattern

def solution(pattern: str, s: str) -> bool:
    words: list[str] = s.split()
    if len(pattern) != len(words):
        return False
    visited: set[str] = set()
    matches: dict[str, str] = {}
    for key, word in zip(pattern, words):
        if key not in matches and word in visited:
            return False
        if key in matches and matches[key] != word:
            return False
        matches[key]: str = word
        visited.add(word)
    return True
    