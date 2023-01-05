# [ LeetCode ] 452. Minimum Number of Arrows to Burst Balloons

def solution(points: list[int]) -> int:
    answer: int = 1
    points.sort(key=lambda point: (point[1], point[0]))
    previous_end: int = points[0][1]
    for start, end in points:
        if start > previous_end:
            answer += 1
            previous_end = end
    return answer
