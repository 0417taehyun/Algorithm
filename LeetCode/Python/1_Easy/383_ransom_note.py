# [ LeetCode ] 383. Ransom Note

def solution(ransomNote: str, magazine: str) -> bool:
    characters: dict[str, int] = {}
    for character in ransomNote:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    for character in magazine:
        if character in characters and characters[character] > 0:
            characters[character] -= 1
        
    return True if sum(characters.values()) == 0 else False


def another_solution(ransomNote: str, magazine: str) -> bool:
    characters: dict[str, int] = {}
    for character in magazine:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    for character in ransomNote:
        if character not in characters or characters[character] == 0:
            return False
        else:
            characters[character] -= 1
        
    return True
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | int]] = [
        {
            "input": {
                "ransomNote": "a",
                "magazine": "b"
            },
            "output": False
        },
        {
            "input": {
                "ransomNote": "aa",
                "magazine": "ab"
            },
            "output": False
        },
        {
            "input": {
                "ransomNote": "aa",
                "magazine": "aab"
            },
            "output": True
        },
        {
            "input": {
                "ransomNote": "aab",
                "magazine": "aabb"
            },
            "output": True
        },
        {
            "input": {
                "ransomNote": "aabbc",
                "magazine": "aabb"
            },
            "output": False
        }                     
    ]
    for case in cases:
        assert case["output"] == solution(
            ransomNote=case["input"]["ransomNote"],
            magazine=case["input"]["magazine"]
        )
        assert case["output"] == another_solution(
            ransomNote=case["input"]["ransomNote"],
            magazine=case["input"]["magazine"]
        )
        