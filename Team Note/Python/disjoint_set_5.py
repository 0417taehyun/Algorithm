"""
서로소 집합(Disjoint Set): 경로 압축(Path Compression) 및 Union By Rank 방식을 통한 최적화
시간 복잡도: find 메서드 O(A(N)), union 메서드 O(A(N))
공간 복잡도: O(N)

find 메서드에 대해서는 경로 압축(Path Compression)을 통해 최적화한다.
union 메서드에 대해서는 rank 배열을 활용하여 최적화한다.
이렇게 트리의 균형을 맞출 수 있다.

이때 시간 복잡도에 사용된 A 함수는 역전 애커만 함수(Inverse Ackermann Function)를 의미한다.
보통 역전 애커만 함수는 상수 시간으로 여기기 때문에 실질적인 시간 복잡도는 O(1)이라 할 수 있다.
"""

class UnionFind:
    BASE_HEIGHT: int = 1

    def __init__(self, size: int) -> None:
        self.root: list[int] = [ vertex for vertex in range(size) ]
        self.rank: list[int] = [ UnionFind.BASE_HEIGHT for _ in range(size) ]
    
    def find(self, vertex: int) -> None:
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

    def is_connected(self, u: int, v:int) -> bool:
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
                "edges": [[8, 9], [1, 2], [2, 5], [5, 6], [6, 7], [3, 8]],
                "source": 1,
                "destination": 7,
            },
            "output": True
        },
        {
            "input": {
                "size": 10,
                "edges": [[8, 9], [2, 1], [2, 5], [5, 6], [7, 6], [8, 3]],
                "source": 2,
                "destination": 9,
            },
            "output": False
        }        
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
