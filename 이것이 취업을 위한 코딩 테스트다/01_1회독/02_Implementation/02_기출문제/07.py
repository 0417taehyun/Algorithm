# [ 이것이 취업을 위한 코딩 테스트다 ] 구현: 치킨 배달

def calculate_distance(
    N: int, chickens: list[tuple[int, int]], houses: list[tuple[int, int]]
) -> int:
    cumulative_distance: int = 0
    for hx, hy in houses:
        minimum_distance: int = 2*2*(N-1)*N
        for cx, cy in chickens:
            current_distance: int = abs(hx - cx) + abs(hy - cy)
            if minimum_distance > current_distance:
                minimum_distance = current_distance

        cumulative_distance += minimum_distance

    return cumulative_distance


def solution() -> None:
    from itertools import combinations


    N, M = map(int, input().split())

    houses, chickens = [], []
    for i in range(N):
        map_info: list[int] = list(map(int, input().split()))
        for j in range(N):
            if map_info[j] == 1:
                houses.append((i, j))
            
            elif map_info[j] == 2:
                chickens.append((i, j))
    
    answer: int = 2*2*N*(N-1)
    target_chickens: list[tuple(int, int)] = combinations(chickens, M)
    for target_chicken in target_chickens:
        current_distance: int = calculate_distance(
            N=N, chickens=target_chicken, houses=houses
        )
        if answer > current_distance:
            answer = current_distance

    print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch


    def test_example_case(case: dict[str, list | int]) -> None:
        with patch("builtins.input", side_effect=case["input"]):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
            
            output: int = case["output"]
            assert test_stdout.getvalue() == f"{output}\n"

    cases: list[dict[str, list | int]] = [
        {
            "input": [
                "5 3", "0 0 1 0 0", "0 0 2 0 1",
                "0 1 2 0 0", "0 0 1 0 0", "0 0 0 0 2",
            ],
            "output": 5,
        },
        {
            "input": [
                "5 2", "0 2 0 1 0", "1 0 1 0 0", "0 0 0 0 0",
                "2 0 0 1 1", "2 2 0 1 2",
            ],
            "output": 10,
        },
        {
            "input": [
                "5 1", "1 2 0 0 0", "1 2 0 0 0", "1 2 0 0 0",
                "1 2 0 0 0", "1 2 0 0 0",
            ],
            "output": 11,
        },
        {
            "input": [
                "5 1", "1 2 0 2 1", "1 2 0 2 1", "1 2 0 2 1",
                "1 2 0 2 1", "1 2 0 2 1",
            ],
            "output": 32,
        },
    ]
    for case in cases:
        test_example_case(case=case)
