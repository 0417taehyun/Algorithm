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


def disjoint_set_quick_union(
    n: int, edges: list[list[int]], source: int, destination: int
) -> bool:
    class UnionFind:
        def __init__(self, size: int) -> None:
            self.root: list[int] = [ vertex for vertex in range(size) ]
        
        def find(self, vertex: int) -> int:
            while vertex != self.root[vertex]:
                vertex: int = self.root[vertex]
            return vertex
        
        def union(self, u: int, v: int) -> int:
            u_root: int = self.find(u)
            v_root: int = self.find(v)
            if u_root != v_root:
                self.root[v_root]: int = u_root
        
        def is_connected(self, u: int, v:int) -> bool:
            return self.find(u) == self.find(v)


    union_find: UnionFind = UnionFind(n)
    for u, v in edges:
        union_find.union(u, v)
    return union_find.is_connected(source, destination)


def disjoint_set_union_by_rank(
    n: int, edges: list[list[int]], source: int, destination: int
) -> bool:
    class UnionFind:
        BASE_HEIGHT: int = 1
        def __init__(self, size: int) -> None:
            self.root: list[int] = [ vertex for vertex in range(size) ]
            self.rank: list[int] = [
                UnionFind.BASE_HEIGHT for _ in range(size)
            ]

        def find(self, vertex: int) -> int:
            while vertex != self.root[vertex]:
                vertex = self.root[vertex]
            return vertex

        def union(self, u: int, v: int) -> None:
            u_root: int = self.find(u)
            v_root: int = self.find(v)
            if u_root != v_root:
                u_rank: int = self.rank[u_root]
                v_rank: int = self.rank[v_root]
                if u_rank > v_rank:
                    self.root[v_root]: int = u_root
                elif u_rank < v_rank:
                    self.root[u_root]: int = v_root
                else:
                    self.root[v_root]: int = u_root
                    self.rank[u_root] += 1

        def is_connected(self, u: int, v: int) -> bool:
            return self.find(u) == self.find(v)

    
    union_find: UnionFind = UnionFind(n)
    for u, v in edges:
        union_find.union(u, v)
    return union_find.is_connected(source, destination)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, int | list[list[int]]] | bool]] = [
        {
            "input": {
                "n": 1,
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
        assert case["output"] == disjoint_set_quick_union(**case["input"])
        assert case["output"] == disjoint_set_union_by_rank(**case["input"])    
        