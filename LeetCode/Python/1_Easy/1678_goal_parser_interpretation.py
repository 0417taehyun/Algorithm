# [ LeetCode ] 1678. Goal Parser Interpretation

def solution(command: str) -> str:
    import re
    
    
    return re.sub(r"(\(\))", "o", re.sub("(\(al\))", "al", command))


def another_solution(command: str) -> str:
    answer: str = ""
    converted_table: dict[str, str] = { "()": "o", "(al)": "al" }
    
    for character in command:
        if character == "G":
            answer += character
            
        elif character == "(":
            consecutive_word: str = "("
        
        elif character == ")":
            consecutive_word += character
            answer += converted_table[consecutive_word]
            consecutive_word = ""
        
        else:
            consecutive_word += character
    
    return answer


def robust_solution(command: str) -> str:
    answer: str = ""
    consecutive_word: str = ""
    converted_table: dict[str, str] = {"()": "o", "(al)": "al", "G": "G"}
    
    for character in command:
        consecutive_word += character
        if consecutive_word in converted_table:
            answer += converted_table[consecutive_word]
            consecutive_word = ""

    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str]] | str] = [
        {
            "input": {"command": "G()(al)"},
            "output": "Goal"
        },
        {
            "input": {"command": "G()()()()(al)"},
            "output": "Gooooal"
        },
        {
            "input": {"command": "(al)G(al)()()G"},
            "output": "alGalooG"
        }
    ]
    for case in cases:
        assert case["output"] == solution(command=case["input"]["command"])
        assert case["output"] == another_solution(
            command=case["input"]["command"]
        )
        assert case["output"] == robust_solution(
            command=case["input"]["command"]
        )
    