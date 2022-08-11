# [ 백준 ] 2110번: 공유기 설치

def solution() -> None:
    import sys
    
    
    input = sys.stdin.readline
    N, C = map(int, input().split())
    houses = [ int(input()) for _ in range(N) ]

    houses.sort()
    answer = 0
    start, end = 1, houses[-1] - houses[0]
    while start <= end:
        count = 1
        middle = (start + end) // 2
        previous_idx = 0
        previous_distance = end
        for idx in range(1, len(houses)):
            distance = houses[idx] - houses[previous_idx]
            if distance >= middle:
                count += 1
                previous_idx = idx
                if distance < previous_distance:
                    previous_distance = distance
                    
        if count >= C:
            if answer < previous_distance:
                answer = previous_distance
            start = middle + 1
        
        else:
            end = middle - 1

    print(answer)
    
    
if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> str:
        with patch("sys.stdin.readline", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()

        return test_stdout.getvalue()
    
    
    case: dict[str, list[str] | str] = {
        "input": ["5 3", "1", "2", "8", "4", "9"],
        "output": "3\n"
    }
    print(test_example_case(input=case["input"]))
    assert case["output"] == test_example_case(input=case["input"])
    