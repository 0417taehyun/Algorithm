# [ LeetCode ] 1833. Maximum Ice Cream Bars

def solution(costs: list[int], coins: int) -> int:
    answer: int = 0
    costs.sort()
    for cost in costs:
        if cost > coins:
            break
        coins -= cost
        answer += 1
    return answer
