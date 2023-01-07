# [ LeetCode ] 134. Gas Station

def solution(gas: list[int], cost: list[int]) -> int:
    diff: list[int] = [ g - c for g, c in zip(gas, cost) ]
    if sum(diff) < 0:
        return -1
    answer: int = 0
    accumulate: int = 0
    for idx, value in enumerate(diff):
        accumulate += value
        if accumulate < 0:
            answer = idx + 1
            accumulate = 0
    return answer
