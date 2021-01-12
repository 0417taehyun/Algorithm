import re

from collections import Counter


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    # for word in paragraph:
    #     if not word.isalpha():
    #         paragraph = paragraph.replace(word, ' ')
    # words = [ word for word in paragraph.lower().split() if word not in banned ]

    # Using Regular Expression
    words = [
        word for word in re.sub('[^a-zA-Z\s]', ' ', paragraph).lower().split()
        if word not in banned
    ]

    result = Counter(words).most_common(1)[0][0]

    return result


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(mostCommonWord(paragraph, banned))
