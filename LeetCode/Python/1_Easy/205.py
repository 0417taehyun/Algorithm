# [ LeetCode ] 205. Isomorphic Strings

def solution(s: str, t: str) -> bool:
    seen: set[str] = set()
    matches: dict[str, str] = {}
    for key, value in zip(s, t):
        if key not in matches and value in seen:
            return False
        if key in matches and matches[key] != value:
            return False
        matches[key]: str = value
        seen.add(value)
    return True
