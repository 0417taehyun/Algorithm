# [ LeetCode ] 389. Find the Difference

def solution(s: str, t: str) -> str:
    characters: dict[str, int] = {}
    for character in s:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    for character in t:
        if character in characters:
            if characters[character] == 0:
                return character
            
            else:
                characters[character] -= 1
        else:
            return character


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": {
                "s": "abcd",
                "t": "abcde",
            },
            "output": "e"
        },
        {
            "input": {
                "s": "",
                "t": "y",
            },
            "output": "y"
        }        
    ]
    for case in cases:
        assert case["output"] == solution(
            s=case["input"]["s"], t=case["input"]["t"]
        )
    