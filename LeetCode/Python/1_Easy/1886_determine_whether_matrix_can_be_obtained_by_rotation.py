# [ LeetCode ] 1886. Determine Whether Matrix Can Be Obtained By Rotation

def solution(mat: list[list[int]], target: list[list[int]]) -> bool:
    def rotate(arr: list[list[int]]) -> None:
        for i in range(len(arr)):
            for j in range(i, len(arr[0])):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        
        for i in range(len(arr)):
            for j in range(len(arr) // 2):
                arr[i][j], arr[i][len(arr)-j-1] \
                    = arr[i][len(arr)-j-1], arr[i][j]
    
    
    count: int = 0
    while count <= 3:
        if mat == target:
            return True
        else:
            rotate(arr=mat)
            count += 1
    
    return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[list[int]]] | bool]] = [
        {
            "input": {
                "mat": [[0, 1],[1, 0]],
                "target": [[1, 0],[0, 1]]
            },
            "output": True,
        },
        {
            "input": {
                "mat": [[0, 1],[1, 1]],
                "target": [[1, 0],[0, 1]]
            },
            "output": False,
        },
        {
            "input": {
                "mat": [[0, 0, 0],[0, 1, 0],[1, 1, 1]],
                "target":  [[1, 1, 1],[0, 1, 0],[0, 0, 0]]
            },
            "output": True,
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
    