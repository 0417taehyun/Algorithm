# [ LeetCode ] 541. Reverse String II

def solution(s: str, k: int) -> str:
    answer: str = ""
        
    idx: int = 1
    temp_origin, temp_reverse = [], []
    for character in s:
        if idx == k * 2:
            for _ in range(len(temp_reverse)):
                answer += temp_reverse.pop()
                
            for origin_character in temp_origin:
                answer += origin_character
            
            answer += character
            
            idx = 0
            temp_origin, temp_reverse = [], []
        
        elif idx <= k:
            temp_reverse.append(character)
        
        else:
            temp_origin.append(character)
        
        idx += 1
    
    if temp_reverse:
        for _ in range(len(temp_reverse)):
            answer += temp_reverse.pop()
    
        if temp_origin:
            for character in temp_origin:
                answer += character

    return answer
            

def another_solution(s: str, k: int) -> str:
    characters: list[str] = list(s)
    for idx in range(0, len(s), 2 * k):
        characters[idx:idx+k] = reversed(characters[idx:idx+k])
    
    return "".join(characters)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str | int] | int]] = [
        {
            "input": { "s": "abcdefg", "k": 2 },
            "output": "bacdfeg"
        },
        {
            "input": { "s": "abcd", "k": 2 },
            "output": "bacd"
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
