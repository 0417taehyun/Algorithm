# [ 백준 ] 11399번: ATM

def solution() -> None:
    N: int = int(input())
    P: list[int] = list(map(int, input().split(" ")))


    P.sort()
    answer: list[int] = [P[0]]

    for idx in range(1, len(P)):
        answer.append(answer[idx - 1] + P[idx])

    print(sum(answer))


def another_solution() -> None:
    N: int = int(input())
    P: list[int] = list(map(int, input().split(" ")))
    
    current: int = 0
    answer: int = 0
    
    P.sort()
    for num in P:
        current += num
        answer += current
    
    print(answer)
    

if __name__ == "__main__":
    import io
    import unittest.mock

    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=["5", "3 1 2 4 3"]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "32\n"
            
            
    test_example_case()
    