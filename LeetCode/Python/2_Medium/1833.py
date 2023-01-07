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


def count_sort_solution(costs: list[int], coins: int) -> int:
    max_cost: int = max(costs)
    bucket: list[int] = [0] * (max_cost + 1)
    for cost in costs:
        bucket[cost] += 1
    answer: int = 0
    for cost in range(1, max_cost+1):
        if not bucket[cost]:
            continue
        count: int = min(bucket[cost], coins//cost)
        answer += count
        coins -= (cost * count) 
    return answer
