# [ LeetCode ] 1657. Determine if Two Strings Are Close

from collections import defaultdict


def get_count_words(words: str) -> dict[str, int]:
    word_count: dict[str, int] = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count


def get_word_count_numbers(word_count: dict[str, int]) -> dict[str, int]:
    word_count_numbers: dict[str, int] = defaultdict(int)
    for count in word_count.values():
        word_count_numbers[count] += 1
    return word_count_numbers


def get_distinct_words(words: str) -> set[str]:
    distinct_words: set[str] = set()
    for word in words:
        if word not in distinct_words:
            distinct_words.add(word)
    return distinct_words


def solution(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    word1_count: dict[str, int] = get_count_words(word1)
    word1_count_numbers: dict[str, int] = get_word_count_numbers(word1_count)
    distinct_word1: set[str] = get_distinct_words(word1)

    word2_count: dict[str, int] = get_count_words(word2)
    word2_count_numbers: dict[str, int] = get_word_count_numbers(word2_count)
    distinct_word2: set[str] = get_distinct_words(word2)

    return (
        word1_count_numbers == word2_count_numbers
        and
        distinct_word1 == distinct_word2
    )
    

if __name__ == "__main__":
    cases: dict[str, dict[str, str] | bool] = [
        {
            "input": {
                "word1": "abc",
                "word2": "bca"
            },
            "output": True
        },
        {
            "input": {
                "word1": "a",
                "word2": "aa"
            },
            "output": False
        },
        {
            "input": {
                "word1": "cabbba",
                "word2": "abbccc"
            },
            "output": True
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        