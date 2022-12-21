"""
서로소 집합(Disjoint Set): Quick Union 구현
시간 복잡도: find 메서드 O(N), union 메서드 O(N)
공간 복잡도: O(N)

Quick Find 구현의 경우 find 메서드가 O(1)이지만 union 메서드는 항상 O(N)이다.
Quick Union 구현의 경우 링크드 리스트(Linked List) 형태로 트리가 구현되는 경우가 최악의 상황이다.
이럴 때만 해당 길이 만큼인 N번 만큼 순회해서 루트를 찾아야 하기 때문에 시간 복잡도가 O(N)이 된다.
따라서 최악의 경우 시간 복잡도가 O(N)이지만 평균적으로 그보다 최선의 상황이 나오기 때문에 Quick Find 구현보다 최적화되어 있다.

추가적으로 이렇게 루트를 찾을 경우 Quick Find 구현과 달리 정렬 여부와 상관 없이 부모 정점을 찾을 수 있다는 장점이 있다.
"""

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root: list[int] = [ vertex for vertex in range(size) ]

    def find(self, vertex: int) -> int:
        while vertex != self.root[vertex]:
            vertex: int = self.root[vertex]
        return vertex

    def union(self, u: int, v: int) -> None:
        u_root: int = self.find(u)
        v_root: int = self.find(v)
        if u_root != v_root:
            self.root[v_root]: int = u_root

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
