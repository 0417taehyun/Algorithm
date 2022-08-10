# [ 백준 ] 1966번: 프린터 큐

def solution() -> None:
    for _ in range(int(input())):
        N, M = map(int, input().split())
        queue: list[int] = list(map(int, input().split()))
        check: list[bool] = [ False for _ in range(N) ]
        check[M]: bool = True
        count: int = 0
        while queue:
            highest_priority: int = max(queue)
            target: int = queue.pop(0)
            is_target: bool = check.pop(0)
            if target == highest_priority:
                count += 1
                if is_target:
                    print(count)
                    break
                
            else:
                queue.append(target)
                check.append(is_target)
    


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch


    def test_example_case(input: list[int]) -> str:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
                
        return test_stdout.getvalue()
            
            
    case: dict[str, list[str] | str] = {
        "input": [
            "3", "1 0", "5", "4 2", "1 2 3 4", "6 0", "1 1 9 1 1 1"
        ],
        "output": "1\n2\n5\n"             
    }
    assert case["output"] == test_example_case(input=case["input"])
        