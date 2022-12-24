# [ LeetCode ] 1779. Find Nearest Point That Has the Same X or Y Coordinate

def solution(x: int, y: int, points: list[list[int]]) -> int:
    answer: int = -1
    previous_distance: int = 2 * (10 ** 4)
    for idx, (target_x, target_y) in enumerate(points):
        if x == target_x or y == target_y:
            target_distance: int = abs(x - target_x) + abs(y - target_y)
            if target_distance < previous_distance:
                previous_distance = target_distance
                answer = idx
    return answer


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int | list[list[int]]]] | int] = [
        {
            "input": {
                "x": 3,
                "y": 4,
                "points": [[1,2],[3,1],[2,4],[2,3],[4,4]]
            },
            "output": 2
        },
        {
            "input": {
                "x": 3,
                "y": 4,
                "points": [[3,4]]
            },
            "output": 0
        },
        {
            "input": {
                "x": 3,
                "y": 4,
                "points": [[2,3]]
            },
            "output": -1
        },        
    ]
    for case in cases:
        assert case["output"] == solution(
            x=case["input"]["x"],
            y=case["input"]["y"],
            points=case["input"]["points"]
        )
    