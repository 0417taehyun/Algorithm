# [ 백준 ] 1157번: 단어 공부

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    word: dict[str, int] = {}
    for alphabet in input().rstrip():
        upper_alphabet = alphabet.upper()
        if upper_alphabet in word:
            word[upper_alphabet] += 1
        else:
            word[upper_alphabet] = 1

    sorted_word = sorted(word.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_word) > 1 and sorted_word[0][1] == sorted_word[1][1]:
        print("?")
    else:
        print(sorted_word[0][0])


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()

    cases: list[dict[str, list[str] | str]] = [
        {
            "input": ["Mississipi"],
            "output": "?\n",
        },
        {
            "input": ["zZa"],
            "output": "Z\n",
        },
        {
            "input": ["z"],
            "output": "Z\n",
        },
        {
            "input": ["baaa"],
            "output": "A\n",
        },
        {
            "input": ["aabbccc"],
            "output": "C\n",
        },
        {
            "input": ["zxcasdqwex"],
            "output": "X\n",
        },
        {
            "input": ["abcdefghijklmnopqrstuvwxyz"],
            "output": "?\n",
        },
        {
            "input": ["Zz"],
            "output": "Z\n",
        },
        {
            "input": ["a"],
            "output": "A\n",
        }                                       
    ]
    for case in cases:
        assert case["output"] == test_example_case(input=case["input"])
    