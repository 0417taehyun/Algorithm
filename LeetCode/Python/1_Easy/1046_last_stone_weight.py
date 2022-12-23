# [ LeetCode ] 1046. Last Stone Weight

def solution(stones: list[int]) -> int:
    import heapq


    negative_stones: list[int] = [ -stone for stone in stones ]
    heapq.heapify(negative_stones)
    while len(negative_stones) > 1:
        first: int = heapq.heappop(negative_stones)
        second: int = heapq.heappop(negative_stones)
        if first != second:
            target: int = first - second
            heapq.heappush(negative_stones, target)
    if not negative_stones:
        return 0
    return -heapq.heappop(negative_stones)


def another_solution(stones: list[int]) -> int:
    max_weight: int = max(stones)
    bucket: list[int] = [0 for _ in range(max_weight+1)]
    for weight in stones:
        bucket[weight] += 1
    


if __name__ == "__main__":
    cases: list[dict[str, dict[list[int]] | int]] = [
        {
            "input": { "stones": [] },
            "output": 0
        },
        {
            "input": { "stones": [] },
            "output": 0
        },
        {
            "input": { "stones": [2, 2] },
            "output": 0
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
