# [ LeetCode ] 323. Number of Connected Components in an Undirected Graph

def solution(n: int, edges: list[list[int]]) -> int:
    graph: dict[int, set[int]] = { vertex: set() for vertex in range(n) }
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    answer: int = 0
    visited: set[int] = set()
    for vertex, connected_vertices in graph.items():
        if vertex not in visited:
            answer += 1
            visited.add(vertex)
            while connected_vertices:
                connected_vertex: int = connected_vertices.pop()
                visited.add(connected_vertex)
                target_vertices: set[int] = graph[connected_vertex] - visited
                for target_vertex in target_vertices:
                    connected_vertices.add(target_vertex)
                    visited.add(target_vertex)
    return answer


def another_solution(n: int, edges: list[list[int]]) -> int:
    def dfs(
        vertex: int, visited: set[int], graph: dict[int, set[int]]
    ) -> None:
        if vertex not in visited:
            visited.add(vertex)
            for connected_vertex in graph[vertex]:
                dfs(connected_vertex, visited, graph)

    answer: int = 0
    graph: dict[int, set[int]] = { vertex: set() for vertex in range(n) }
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    visited: set[int] = set()
    for vertex in graph.keys():
        if vertex not in visited:
            answer += 1
            dfs(vertex, visited, graph)
    
    return answer


def disjoint_set_quick_union(n: int, edges: list[list[int]]) -> int:
    class UnionFind:
        def __init__(self, size: int) -> None:
            self.root: list[int] = [ vertex for vertex in range(size) ]
        
        def find(self, vertex: int) -> int:
            while vertex != self.root[vertex]:
                vertex = self.root[vertex]
            return vertex

        def union(self, u: int, v: int) -> None:
            u_root: int = self.find(u)
            v_root: int = self.find(v)
            if u_root != v_root:
                self.root[v_root]: int = u_root
        

    root_vertices: set[int] = set()
    vertices: set[int] = { vertex for vertex in range(n) }
    union_find: UnionFind = UnionFind(n)
    for u, v in edges:
        union_find.union(u, v)
    for vertex in vertices:
        root: int = union_find.find(vertex)
        if root not in root_vertices:
            root_vertices.add(root)
    return len(root_vertices)


def disjoint_set_path_compression_and_union_by_rank(
    n: int, edges: list[list[int]]
) -> int:
    class UnionFind:
        BASE_HEIGHT: int = 1

        def __init__(self, size: int) -> None:
            self.root: list[int] = [ vertex for vertex in range(size) ]
            self.rank: list[int] = [
                UnionFind.BASE_HEIGHT for _ in range(size)
            ]

        def find(self, vertex: int) -> int:
            if vertex == self.root[vertex]:
                return vertex
            self.root[vertex]: int = self.find(self.root[vertex])
            return self.root[vertex]
        
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

    
    union_find: UnionFind = UnionFind(n)
    for u, v in edges:
        union_find.union(u, v)
    for vertex in range(n):
        union_find.find(vertex)
    return len(set(union_find.root))


if __name__ == "__main__":
    cases: list[dict[str, dict[int, list[int]] | int]] = [
        {
            "input": {
                "n": 5,
                "edges": [[0, 1], [1, 2], [3, 4]]
            },
            "output": 2
        },
        {
            "input": {
                "n": 5,
                "edges": [[0, 1], [1, 2], [2, 3], [3, 4]]
            },
            "output": 1
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
        assert case["output"] == disjoint_set_quick_union(**case["input"])
        assert case["output"] == disjoint_set_path_compression_and_union_by_rank(
            **case["input"]
        )
