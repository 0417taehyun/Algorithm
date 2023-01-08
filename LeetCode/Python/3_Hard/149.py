# [ LeetCode ] 149. Max Points on a Line

def solution(points: list[int]) -> int:
    from math import inf
    from collections import defaultdict


    answer: int = 1
    for i in range(len(points)-1):
        start_x, start_y = points[i]
        gradients: dict[float, int] = defaultdict(int)
        for j in range(i+1, len(points)):
            gradient: float = float(inf)
            current_x, current_y = points[j]
            if current_x != start_x:
                gradient = (current_y - start_y) / (current_x - start_x)
            gradients[gradient] += 1
        answer = max(answer, max(gradients.values()) + 1)
    return answer
