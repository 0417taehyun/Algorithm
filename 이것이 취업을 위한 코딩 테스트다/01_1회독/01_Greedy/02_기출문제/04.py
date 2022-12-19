# [ 이것이 취업을 위한 코딩 테스트다 ] 그리디: 문자열 뒤집기

def solution() -> None:
    N: int = int(input())
    coins: list[int] = list(map(int, input().split()))
    
    max_price: int = sum(coins)
    possible_price: dict[int, int] = { number: 0 for number in range(1, max_price + 1) }
    
    for i in range(len(coins)):
        for j in range(i + 1, len(coins) + 1):
            possible_price[sum(coins[i:j])] += 1
    
    for price in range(1, max_price + 2):
        if not possible_price[price]:
            print(price)
            break


def best_solution() -> None:
    N: int = int(input())
    coins: list[int] = list(map(int, input().split()))
    
    coins.sort()
    target: int = 1
    for coin in coins:
        if target < coin:
            break
            
        target += coin
    
    print(target)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case() -> None:
        with patch("builtins.input", side_effect=["5", "3 2 1 1 9"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
            assert test_stdout.getvalue() == "8\n"
    
    
    test_example_case()
    