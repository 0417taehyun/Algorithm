"""
서로소 집합(Disjoint Set): Union By Rank 구현
시간 복잡도: find 메서드 O(logN), union 메서드 O(logN)
공간 복잡도: O(N)

트리의 균형(Balance)을 맞춘다고 생각하면 편하다.
이때 rank는 트리의 높이(Height)를 의미하며 더 큰 높이를 가진 트리에 작은 높이의 트리를 병합한다.
이렇게 되면 트리의 균형이 최대한 맞춰지기 때문에 각 메서드에 대해 시간 복잡도를 로그 시간을 취할 수 있다.
"""

class UnionFind:
    BASE_HEIGHT: int = 1

    def __init__(self, size: int) -> None:
        self.root: list[int] = [ vertex for vertex in range(size) ]
        self.rank: list[int] = [ UnionFind.BASE_HEIGHT for _ in range(size) ]
    
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
