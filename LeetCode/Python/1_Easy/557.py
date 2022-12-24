# [ LeetCode ] 557. Reverse Words in a String III

def solution(s: str) -> str:
    answer: str = ""
    temp: list[str] = []
    for character in s:
        if character == " ":
            for _ in range(len(temp)):
                answer += temp.pop()
            answer += " "
        else:
            temp.append(character)
    
    for _ in range(len(temp)):
        answer += temp.pop()
        
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": { "s": "Let's take LeetCode contest" },
            "output": "s'teL ekat edoCteeL tsetnoc"
        },
        {
            "input": { "s": "God Ding" },
            "output": "doG gniD"
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
    