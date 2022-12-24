# [ LeetCode ] 1167. Minimum Cost to Connect Sticks

def solution(sticks: list[int]) -> int:
    import heapq


    answer: int = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
        first: int = heapq.heappop(sticks)
        second: int = heapq.heappop(sticks)
        accumulate: int = first + second
        heapq.heappush(sticks, accumulate)
        answer += accumulate
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int]] | int]] = [
        {
            "input": { "sticks": [2, 4, 3] },
            "output": 14
        },
        {
            "input": { "sticks": [1, 8, 3, 5] },
            "output": 30
        },
        {
            "input": { "sticks": [5] },
            "output": 0
        },
        {
            "input": { "sticks": [3, 7, 1, 10, 8] },
            "output": 62
        }                            
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
