# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 문자열 재정렬

def solution() -> None:
    S: str = input()

    only_characters: str = ""
    cumulative_number: int = 0
    for character in S:
        if character.isnumeric():
            cumulative_number += int(character)

        else:
            only_characters += character
    
    answer = "".join(sorted(only_characters)) + str(cumulative_number)
    print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["K1KA5CB7"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()

            assert test_stdout.getvalue() == "ABCKK13\n"
    

    test_example_case()
