# [ LeetCode ] 1309. Decrypt String from Alphabet to Integer Mapping

def solution(s: str) -> str:
    digit_to_alphabet: dict[str, str] = {}
    number: int = 1
    for ascii_code in range(ord('a'), ord('z') + 1):
        if number < 10:
            digit_to_alphabet[str(number)] = chr(ascii_code)
        else:
            digit_to_alphabet[f"{number}#"] = chr(ascii_code)
        
        number += 1
    
    answer: str = ""
    stack: list[str] = []
    consecutive_times: int = 0
    for letter in s[::-1]:
        if letter == "#":
            stack.append(letter)
            consecutive_times += 1
        else:
            if stack:
                if consecutive_times == 2:
                    target: str = letter + "".join(stack[::-1])
                    answer = digit_to_alphabet[target] + answer
                    
                    stack = []
                    consecutive_times = 0
                else:
                    stack.append(letter)
                    consecutive_times += 1
            
            else:
                answer = digit_to_alphabet[letter] + answer
    
    return answer
                

def another_solution(s: str) -> str:
    answer: str = ""
    diff: int = ord("a") - 1
    list_s: list[str] = list(s)
    
    while list_s:
        letter: str = list_s.pop()
        if letter == "#":
            target: str = list_s.pop() + list_s.pop()
            answer = chr(int(target[::-1]) + diff) + answer
        
        else:
            answer = chr(int(letter) + diff) + answer

    return answer


def regex_solution(s: str) -> str:
    import re
    
    
    diff: int = ord('a') - 1
    results: list[str] = re.findall(r"\d\d\#|\d", s)
    return "".join([ chr(int(result[:2]) + diff) for result in results ])
    
    
if __name__ == "__main__":
    cases: list[dict[str, dict[str, ] | bool]] = [
        {
            "input": { "s": "10#11#12" },
            "output": "jkab"
        },
        {
            "input": { "s": "1326#" },
            "output": "acz"
        }        
    ]
    for case in cases:
        assert case["output"] == solution(s=case["input"]["s"])
        assert case["output"] == another_solution(s=case["input"]["s"])
        assert case["output"] == regex_solution(s=case["input"]["s"])
    