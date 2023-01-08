# [ LeetCode ] 2214. Minimum Health to Beat Game

def solution(damage: list[int], armor: int) -> int:
    answer: int = 1
    max_damage: int = 0
    for current in damage:
        answer += current
        max_damage = max(max_damage, current)
    return answer - min(max_damage, armor)
    