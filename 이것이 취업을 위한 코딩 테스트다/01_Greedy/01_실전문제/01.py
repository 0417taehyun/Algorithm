# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 큰 수의 법칙

def solution() -> None:
    N, M, K = list(map(int, input().split(" ")))
    numbers: list[int] = list(map(int, input().split(" ")))
    
    numbers.sort(reverse=True)
    largest_number: int = numbers[0]
    second_number: int = numbers[1]
    
    set_count = M // (K + 1)
    remained_count = M % (K + 1)
    
    answer: int = (
        (largest_number * K + second_number) * set_count
        +
        largest_number * remained_count
    )
    
    print(answer)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["5 8 3", "2 4 5 4 6"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "46\n"
    
    
    test_example_case()
    