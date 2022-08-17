# [ LeetCode ] 242. Valid Anagram

def solution(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def another_solution(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    else:
        characters: dict[str, int] = {}
        for character in s:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
        
        for character in t:
            if character in characters:
                if characters[character] > 0:
                    characters[character] -=1
                else:
                    return False
            else:
                return False
            
        return True


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | bool]] = [
        {
            "input": {
                "s": "anagram",
                "t": "nagaram",
            },
            "output": True
        },
        {
            "input": {
                "s": "rat",
                "t": "car",
            },
            "output": False
        },
        {
            "input": {
                "s": "a",
                "t": "ab",
            },
            "output": False
        }          
    ]
    for case in cases:
        assert case["output"] == solution(
            s=case["input"]["s"], t=case["input"]["t"]
        )
        assert case["output"] == another_solution(
            s=case["input"]["s"], t=case["input"]["t"]
        )        
    