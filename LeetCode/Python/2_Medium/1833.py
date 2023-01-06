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


def another_solution(costs: list[int], coins: int) -> int:
    import heapq


    answer: int = 0
    heapq.heapify(costs)
    while costs:
        cost: int = heapq.heappop(costs)
        if coins < cost:
            break
        coins -= cost
        answer += 1
    return answer
