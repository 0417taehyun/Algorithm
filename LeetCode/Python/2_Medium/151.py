# [ LeetCode ] 151. Reverse Words in a String

def solution(s: str) -> str:
    stack: list[str] = []
    temporary: str = ""
    for letter in s:
        if letter == " ":
            if temporary:
                stack.append(temporary)
                temporary = ""
        else:
            temporary += letter
    
    if temporary:
        stack.append(temporary)

    answer: str = ""
    while stack:
        word: str = stack.pop()
        answer += (word + " ")
    answer = answer.rstrip()
    return answer


def another_solution(s: str) -> str:
    from collections import deque


    queue: deque = deque()
    s = s.strip()
    temporary: str = ""
    for letter in s:
        if letter == " " and temporary:
            queue.appendleft(temporary)
            temporary = ""
        elif letter != " ":
            temporary += letter
    queue.appendleft(temporary)

    answer: str = " ".join(queue)
    return answer


def inplace_solution(s: str) -> str:
    def is_need_to_add_space(target: int, words: str) -> bool:
        if words[target] != " ":
            return False
        if words[target-1] != " ":
            return True
        return False


    def remove_multiple_spaces(s: str) -> list[str]:
        words: list[str] = []
        for idx, word in enumerate(s):
            if is_need_to_add_space(idx, s):
                words.append(word)
            elif word != " ":
                words.append(word)
        return words


    def reverse_word(left: int, right: int, words: list[str]) -> None:
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1


    s = s.strip()
    words: list[str] = remove_multiple_spaces(s)
    left: int = 0
    reverse_word(left, len(words)-1, words)
    for idx, letter in enumerate(words):
        if letter == " ":
            reverse_word(left, idx-1, words)
            left = idx + 1
    reverse_word(left, len(words)-1, words)
    answer: str = ""
    for letter in words:
        answer += letter
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | str]] = [
        {
            "input": {"s": "the sky is blue"},
            "output": "blue is sky the"
        },
        {
            "input": {"s": "  hello world  "},
            "output": "world hello"
        },
        {
            "input": {"s": "a good   example"},
            "output": "example good a"
        }     
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == inplace_solution(**case["input"])
