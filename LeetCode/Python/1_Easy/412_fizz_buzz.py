# [ LeetCode ] 412. Fizz Buzz

def solution(n: int) -> list[str]:
    FIZZ: str = "Fizz"
    BUZZ: str = "Buzz"
    FIZZ_BUZZ: str = "FizzBuzz"


    def get_string(index: int) -> str:
        if (index % 3 == 0) and (index % 5 == 0):
            return FIZZ_BUZZ
        if index % 3 == 0:
            return FIZZ
        if index % 5 == 0:
            return BUZZ
        return str(index)


    answer: list[str] = []
    for idx in range(1, n+1):
        target: str = get_string(idx)
        answer.append(target)
    return answer


def another_solution(n: int) -> list[str]:
    DIVISORS: list[int] = [3, 5]
    WORDS: dict[int, str] = {3: "Fizz", 5: "Buzz"}


    answer: list[str] = []
    for idx in range(1, n+1):
        temporary_word: list[str] = []
        for divisor in DIVISORS:
            if idx % divisor == 0:
                temporary_word.append(WORDS[divisor])

        if not temporary_word:
            temporary_word.append(str(idx))

        target: str = "".join(temporary_word)
        answer.append(target)

    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int] | list[str]]] = [
        {
            "input": { "n": 3 },
            "output": ["1", "2", "Fizz"]
        },
        {
            "input": { "n": 5 },
            "output": ["1", "2", "Fizz", "4", "Buzz"]
        },
        {
            "input": { "n": 15 },
            "output": [
                "1", "2", "Fizz", "4", "Buzz",
                "Fizz", "7", "8", "Fizz", "Buzz",
                "11", "Fizz", "13", "14", "FizzBuzz"
            ]
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
