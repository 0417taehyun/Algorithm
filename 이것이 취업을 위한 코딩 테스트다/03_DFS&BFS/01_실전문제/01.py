# [ 이것이 취업을 위한 코딩 테스트다 ] DFS/BFS: 음료수 얼려 먹기

def solution() -> None:
    N, M = map(int, input().split())
    graph: list[list[int]] = [ list(map(int, input())) for _ in range(N) ]

    
    def dfs(x: int, y: int) -> bool:
        if (x == -1) or (y == -1) or (x == N) or (y == M):
            return False
        
        else:
            if not graph[x][y]:
                graph[x][y] = 1
                
                dfs(x=x-1, y=y)
                dfs(x=x, y=y-1)
                dfs(x=x+1, y=y)
                dfs(x=x, y=y+1)

                return True
        
            else:
                return False
    
    
    answer: int = 0
    for i in range(N):
        for j in range(M):
            if dfs(x=i, y=j):
                answer += 1
        
    print(answer)
    

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch
    
    
    def test_example_case(input: list[str]) -> int:
        with patch("builtins.input", side_effect=input):
            with patch("sys.stdout", new_callable=StringIO) as test_stdout:
                solution()
        
        return test_stdout.getvalue()
    
    
    cases: list[dict[str, list[str] | int]] = [
        {
            "input": ["4 5", "00110", "00011", "11111", "00000"],
            "output": 3,
        },
        {
            "input": ["3 3", "001", "010", "101"],
            "output": 3,            
        }
    ]
    for case in cases:
        output: int = case["output"]
        assert f"{output}\n" == test_example_case(input=case["input"])
    