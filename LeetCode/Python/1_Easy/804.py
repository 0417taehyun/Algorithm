# [ LeetCode ] 804. Unique Morse Code Words

def solution(words: list[str]) -> int:
    morse_codes: list[str] = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    alphabet_to_morse_codes: dict[str, str] = {
        chr(ord("a") + idx): morse_codes[idx]
        for idx in range(len(morse_codes)) 
    }
    seen: set = set()
    for word in words:
        seen.add(
            "".join(
                [ alphabet_to_morse_codes[alphabet] for alphabet in word ]
            )
        )
    
    return len(seen)
        


def another_solution(words: list[int]) -> int:
    import string
    morse_codes: list[str] = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]    
    alphabet_to_morse_codes: dict[str, str] = {
        alphabet: morse_code for alphabet, morse_code
        in zip(string.ascii_lowercase, morse_codes)   
    }
    seen: set = set()
    for word in words:
        seen.add(
            "".join(
                [ alphabet_to_morse_codes[alphabet] for alphabet in word ]
            )
        )
    
    return len(seen)

    
if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[str]]] | int] = [
        {
            "input": {"words": ["gin","zen","gig","msg"]},
            "output": 2
        },
        {
            "input": {"words": ["a"]},
            "output": 1
        },        
    ]
    for case in cases:
        assert case["output"] == solution(words=case["input"]["words"])
        assert case["output"] == another_solution(words=case["input"]["words"])