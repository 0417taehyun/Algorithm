# [ LeetCode ] 387. First Unique Character in a String

def solution(s: str) -> int:
    characters: dict[str, int] = {}
    for idx, character in enumerate(s):
        if character in characters:
            characters[character] = -1
        else:
            characters[character] = idx
            
    indexes: list[int] = sorted(characters.values())
    for idx in indexes:
        if idx != -1:
            return idx
    
    return -1


def another_solution(s: str) -> int:
    characters: dict[str, int] = {}
    seen: set = set()
    for idx, character in enumerate(s):
        if character in seen and character in characters:
            characters.pop(character)

        elif character not in seen:
            seen.add(character)
            characters[character] = idx
        
    
    return next(iter(characters.values())) if characters else -1


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str]] | int] = [
        {
            "input": {"s": "leetcode"},
            "output": 0
        },
        {
            "input": {"s": "loveleetcode"},
            "output": 2
        },
        {
            "input": {"s": "aabb"},
            "output": -1
        }                
    ]
    for case in cases:
        assert case["output"] == solution(s=case["input"]["s"])
        assert case["output"] == another_solution(s=case["input"]["s"])
    