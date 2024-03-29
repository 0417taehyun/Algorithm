# [ 백준 ] 2217번: 로프

def solution() -> None:
    N: int = int(input())
    ropes: list[int] = [ int(input()) for _ in range(N) ]

    ropes.sort(reverse=True)
    answer: int = ropes[0]
    for idx, weight in enumerate(ropes):
        if (current_weight := weight * (idx + 1)) > answer:
            answer = current_weight

    print(answer)
        

def short_solution() -> None:
    N: int = int(input())
    ropes: list[int] = [ int(input()) for _ in range(N) ]
    
    print(max([
        weight * (idx + 1) for idx, weight
        in enumerate(sorted(ropes, reverse=True))
    ]))


if __name__ == "__main__":
    import io
    import unittest.mock
    

    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=["3", "10", "20", "25"]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "40\n"
            
            
    test_example_case()
    