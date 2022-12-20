"""
서로소 집합(Disjoint Set): Quick Find 구현
시간 복잡도: find 메서드 O(1), union 메서드 O(N)
공간 복잡도: O(N)

이때 유의할 점은 정렬되지 않은 상태로 간선이 입력될 경우 오류가 발생한다.
예를 들어 [[4, 3], [2, 3]]에 대한 루트 값은 [0, 1, 2, 2, 4]이 된다.
따라서 2와 4에 대한 정점(Vertex)이 연결되어 있음에도 불구하고 연결되지 않은 것으로 판명된다.
"""

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root: list[int] = [ vertex for vertex in range(size) ]

    def find(self, vertex: int) -> int:
        return self.root[vertex]

    def union(self, u: int, v: int) -> None:
        u_root: int = self.find(u)
        v_root: int = self.find(v)
        if u_root != v_root:
            for parent in self.root:
                if parent == u_root:
                    self.root[v]: int = parent

    def is_connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)


def solution(
    size: int, edges: list[list[int]], source: int, destination: int
) -> bool:
    union_find: UnionFind = UnionFind(size)
    for u, v in edges:
        union_find.union(u, v)
    return union_find.is_connected(source, destination)


if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[int] | int] | bool]] = [
        {
            "input": {
                "size": 10,
                "edges": [[1, 2], [2, 5], [5, 6], [6, 7], [3, 8], [8, 9]],
                "source": 1,
                "destination": 7,
            },
            "output": True
        },
        {
            "input": {
                "size": 10,
                "edges": [[1, 2], [2, 5], [5, 6], [6, 7], [3, 8], [8, 9]],
                "source": 2,
                "destination": 9,
            },
            "output": False
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
