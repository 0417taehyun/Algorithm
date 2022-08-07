# [ LeetCode ] 1232. Check If It Is a Straight Line

def solution(coordinates: list[list[int]]) -> bool:
    coordinates.sort()
    diff_x: int = coordinates[1][0] - coordinates[0][0]
    diff_y: int = coordinates[1][1] - coordinates[0][1]
    for idx in range(1, len(coordinates)-1):
        current_diff_x: int = coordinates[idx+1][0] - coordinates[idx][0]
        current_diff_y: int = coordinates[idx+1][1] - coordinates[idx][1]
        
        if diff_x == 0:
            if current_diff_x != 0:
                return False
        elif diff_y == 0:
            if current_diff_y != 0:
                return False
        else:
            if current_diff_x == 0:
                return False
            
            elif (diff_y / diff_x) != (current_diff_y / current_diff_x):
                return False
    
    return True


def another_solution(coordinates: list[list[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[:2]
    return all( (y1-y0)*(x-x1) == (y-y1)*(x1-x0) for x, y in coordinates[2:] )


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]]]] | bool] = [
        {
            "input": {"coordinates": [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]},
            "output": True,
        },
        {
            "input": {"coordinates": [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]},
            "output": False,
        },
        {
            "input": {"coordinates": [[1,-8],[2,-3],[1,2]]},
            "output": False,
        }                 
    ]
    for case in cases:
        assert case["output"] == solution(
            coordinates=case["input"]["coordinates"]
        )
        assert case["output"] == another_solution(
            coordinates=case["input"]["coordinates"]
        )
