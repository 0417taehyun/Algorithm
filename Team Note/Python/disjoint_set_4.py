"""
서로소 집합(Disjoint Set): 경로 압축 최적화(Pass Compression Optimization)
시간 복잡도: find 메서드 O(logN), union 메서드 O(logN)
공간 복잡도: O(N)

Quick Find 구현의 단점이었던 union 메서드의 최적화를 위한 방법이다.
find 메서드를 사용할 때 root 값을 매번 갱신하여 평균적인 트리의 균형을 맞춘다.
이를 통해 기존 시간 복잡도가 O(N)이던 상황을 평균적으로 O(logN)으로 최적화한다.
이때 재귀(Recursion) 호출을 통해서 함수의 콜 스택(Call Stack)의 루트를 찾아가는 형태로 구현한다.

유의할 점은 Quick Find 구현 때와 마찬가지로 간선이 정렬되지 않은 상태로 입력될 때다.
이를 테면 [[4, 3], [2, 3]]과 같이 간선이 주어질 경우 최종적으로 정점 4의 루트 노드는 정점 4 본인인데 정점 2와 3은 정점 2로 갱신된다.
정점 2, 3, 4가 모두 연결되어 있음에도 불구하고 루트 노트를 통해 해당 정점들이 연결된 것을 알지 못하는 것이다.
"""

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root: list[int] = [ vertex for vertex in range(size) ]
    
    def find(self, vertex: int) -> int:
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]

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
