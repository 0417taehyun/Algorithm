# [ LeetCode ] 2244. Minimum Rounds to Complete All Tasks

def solution(tasks: list[int]) -> int:
    from collections import defaultdict


    answer: int = 0
    counts: dict[int, int] = defaultdict(int)
    for difficulty in tasks:
        counts[difficulty] += 1
    for difficulty, count in counts.items():
        if count == 1:
            return -1
        answer += (count // 3)
        if (count % 3) > 0:
            answer += 1
    return answer
