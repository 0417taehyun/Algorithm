# [ LeetCode ] 1971. Find if Path Exists in Graph

def solution(
    n: int, edges: list[list[int]], source: int, destination: int\
) -> bool:
    from collections import deque, defaultdict


    if source == destination:
        return True
    
    graph: dict[int, set[int]] = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    queue: deque = deque([source])
    visited: set[int] = set([source])
    while queue:
        vertex: int = queue.popleft()
        conncted_vertices: set[int] = graph[vertex] - visited
        for connected_vertex in conncted_vertices:
            if connected_vertex == destination:
                return True
            queue.append(connected_vertex)
            visited.add(connected_vertex)
    return False


def another_solution(
    n: int, edges: list[list[int]], source: int, destination: int
) -> bool:
    from collections import defaultdict


    if source == destination:
        return True

    graph: dict[int, set[int]] = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    stack: list[int] = [source]
    visited: set[int] = set([source])
    while stack:
        vertex: int = stack.pop()
        conncted_vertices: set[int] = graph[vertex] - visited
        for connected_vertex in conncted_vertices:
            if connected_vertex == destination:
                return True
            stack.append(connected_vertex)
            visited.add(connected_vertex)
    return False


def disjoint_set(
    n: int, edges: list[list[int]], source: int, destination: int
) -> bool:
    return 



if __name__ == "__main__":
    cases: list[dict[str, dict[str, int | list[list[int]]] | bool]] = [
        {
            "input": {
                "n": 0,
                "edges": [],
                "source": 0,
                "destination": 0
            },
            "output": True
        },
        {
            "input": {
                "n": 3,
                "edges": [[0, 1], [1, 2], [2, 0]],
                "source": 0,
                "destination": 2
            },
            "output": True
        },
        {
            "input": {
                "n": 6,
                "edges": [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
                "source": 0,
                "destination": 5
            },
            "output": False
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
