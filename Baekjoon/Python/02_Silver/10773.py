# [ 백준 ] 10773번: 제로

def solution() -> None:
    K: int = int(input())
    numbers: list[int] = []
    for _ in range(K):
        if not (number := int(input())):
            numbers.pop()
        else:
            numbers.append(number)
    print(sum(numbers))
        

if __name__ == "__main__":
    import io
    import unittest.mock    
    

    def test_example_case() -> None:
        with unittest.mock.patch("builtins.input", side_effect=[
            "10", "1", "3", "5", "4", "0", "0", "7", "0", "0", "6"
        ]):
            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as test_stdout:
                solution()

        assert test_stdout.getvalue() == "7\n"
            
            
    test_example_case()
    