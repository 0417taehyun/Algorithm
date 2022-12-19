# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 럭키 스트레이트

def solution() -> None:
    N: list[int] = [ int(number) for number in input() ]

    left_sum: int = 0
    right_sum: int = 0
    for idx in range(len(N) // 2):
        left_sum += N[idx]
        right_sum += N[len(N) - idx - 1]

    if left_sum == right_sum:
        print("LUCKY")
    
    else:
        print("READY")


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch


    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["123402"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()

            assert test_stdout.getvalue() == "LUCKY\n"
    

    test_example_case()
