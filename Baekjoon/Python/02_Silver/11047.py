# [ 백준 ] 11047번: 동전 0

def solution() -> None:
    N, K = list(map(int, input().split(" ")))
    A: list[int] = []
    for _ in range(N):
        coin: int = int(input())
        if coin <= K:
            A.insert(0, coin)
    
    answer: int = 0
    for coin in A:
        answer += (K // coin)
        K %= coin
    
    print(answer)
        

if __name__ == "__main__":
    import io
    import unittest.mock


    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=[
            "10 4200",
            "1",
            "5",
            "10",
            "50",
            "100",
            "500",
            "1000",
            "5000",
            "10000",
            "50000",
        ]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "6\n"
            
            
    test_example_case()
    